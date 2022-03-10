from django.shortcuts import redirect, render
from datetime import date
from django.http.response import HttpResponse
from Hotel.models import Hotel
from .models import *
from random import choices,choice,randrange
from django.core.mail import send_mail
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# import uuid
from myapp.models import User

# create your view here

def index(request):
 #   uid = User.objects.get(email=request.session['email'])
    hotel = Hotel.objects.all()[::-1]
    return render(request,'index.html',{'hotel':hotel})

def about(request):
    return render(request,'about.html')

def Aview_hotels(request,pk):
    hotel = Hotel.objects.get(id=pk)
    return render(request,'Aview_hotels.html',{'hotel':hotel})     
   

def hotels2(request):
    hotel = Hotel.objects.all()[::-1]
    return render(request,'hotels2.html',{'hotel':hotel}) 
    
def logout(request):
    del request.session['email']
    return redirect('login')    
           

def login(request):
   # try:
   #     uid = User.objects.get(email=request.session['email'])
   #     return render(request,'index.html')
   # except:
      if request.method == 'POST':
         try:
            uid = User.objects.get(email=request.POST['email'])
            if uid.password == request.POST['password']:
                request.session['email'] = request.POST['email']

                return render(request,'index.html',{'uid':uid})
            else:
                msg = 'Password does not match'
                return render(request,'login.html',{'msg':msg})
         except:
            msg = 'Email is not register'
            return render(request,'login.html',{'msg':msg})
      else:
        return render(request,'login.html')      

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'User already registered'
            return render(request,'register.html',{'msg':msg})
        except:
               request.POST['password'] 
               otp = randrange(1000,9999)
               subject = 'Welcome to Travling app' 
               message = f"""Hello {request.POST['fname']} {request.POST['lname']}
               Your Verification OTP is : {otp}.
               """
               email_from = settings.EMAIL_HOST_USER
               recipient_list = [request.POST['email']]
               send_mail( subject, message, email_from, recipient_list )
               global temp
               temp = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password'],
               }
               return render(request,'otp.html',{'otp':otp}) 

    else:
         return render(request,'register.html')


def otp(request):
    if request.POST:
        if request.POST['otp']:
            global temp
            User.objects.create(
                fname = temp['fname'],
                lname = temp['lname'],
                mobile = temp['mobile'],
                email = temp['email'],
                address = temp['address'],
                password = temp['password'],
            )
            msg = 'User is Created'
            return render(request,'login.html',{'msg':msg}) 
        else:
            msg = 'OTP deos not match'
            return render(request,'otp.html',{'msg':msg,'otp':request.POST['otp']})

    return render(request,'otp.html')


def profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.password = request.POST['password']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        uid.save()
        
    return render(request,'profile.html',{'uid':uid})

def fpassword(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            s = ''.join(choices('abcdefghijklmnopqrstuvwxyz123456789',k=8))
            subject = 'Password has been reset'
            message = f"""Hello user your new password is : {s}
            """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email']]
            send_mail(subject,message,email_from,recipient_list,auth_password='om98045238')
            uid.password = s
            uid.save()
            return render (request,'login.html',{'msg':subject})
        except:
            msg = 'User Is Not Registered'
            return render(request,'login.html',{'msg':msg})
    return render(request,'fpassword.html')



def paymentsuccess(request):
    return render(request,'paymentsuccess.html')





razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def booking(request,bk):
    hotel = Hotel.objects.get(id=bk)
    uid = User.objects.get(email=request.session['email']),

    if request.method == 'POST': 
        

        check_in = request.POST['check_in'].split('-')
        check_out = request.POST['check_out'].split('-')

        indate = date(int(check_in[0]),int(check_in[1]),int(check_in[2]))
        outdate = date(int(check_out[0]),int(check_out[1]),int(check_out[2]))
        day = int((outdate - indate).days)
        # print(day)
        price =  int(request.POST['no_person']) / 4
        if price == int(price):
            price = int(price) * int(hotel.hotel_price) * day
        else:
            price = (int(price)+1) * int(hotel.hotel_price) * day
        request.session['payuser'] = price*100
        request.session['in'] = request.POST['check_in']
        request.session['out'] = request.POST['check_out']
        request.session['person'] = request.POST['no_person']
        
        currency = 'INR'
        amount = price*100 #price*100  # Rs. 200
        
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = f'paymenthandler/{hotel.id}'
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context.update({'hotel':hotel,'uid':uid})
        return render(request,'payment.html',context=context)
    return render(request,'booking.html',{'hotel':hotel})  
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,pk):
    
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                # print(request.session['payuser'], type(request.session['payuser']))
                amount = request.session['payuser']  # Rs. 200
                del request.session['payuser']
                try:
                    
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    # test = uuid.uuid4()
                    # object = bookingUser.objects.create( = test)
                    # geek_object.save()
                    uid = User.objects.get(email=request.session['email'])
                    hotel = Hotel.objects.get(id=pk)
                    # render success page on successful caputre of payment
                    book = BookingUser.objects.create(
                        uid = uid,
                        hname = hotel,
                        check_in = request.session['in'],
                        check_out = request.session['out'],
                        no_person = request.session['person'],
                        bookprice = amount//100,
                        
                    )

                    return render(request, 'paymentsuccess.html',{'book':book})
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

def reservation(request):
    uid = User.objects.get(email=request.session['email'])
    book = BookingUser.objects.filter(uid=uid)[::-1]
    return render(request,'reservation.html',{'books':book})

   



