from django.http.response import HttpResponse
from django.shortcuts import  redirect, render
from Hotel.models import *
from random import choice, choices, randrange
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def hotelsindex(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'hotelsindex.html',{'uid':uid})


def hotelsprofile(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'hotelsprofile.html',{'uid':uid})

def hotelstables(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'hotelstables.html',{'uid':uid})

def hotelsupgrade(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'hotelsupgrade.html',{'uid':uid})

def add_hotels(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Hotel.objects.create(
            uid = uid,
            hotel_name = request.POST['hotelname'],
            hotel_adderss = request.POST['address'],
            hotel_country = request.POST['country'],
            hotel_rooms = int(request.POST['rooms']),
            hotel_mobile = request.POST['mobile'],
            hotel_price = request.POST['price'],
            hotel_wifi = True if request.POST['wifi'] == 'yes' else False,
            hotel_photos = request.FILES['photos'],
            add_details = request.POST['adddetails'],
            hotel_acroom = request.POST['acroom'],

        )
        msg = 'Hotel is Add'
        return render(request,'add-hotels.html',{'uid':uid, 'msg':msg} )      
    return render(request,'add-hotels.html',{'uid':uid} )      

def hotelslogout(request):
    del request.session['email']
    return redirect('hotelslogin')              




def hotelslogin(request):
#    try:
#        uid = User.objects.get(email=request.session['email'])
#        return render(request,'hotelsindex.html')
#    except:
      if request.method == 'POST':
         try:
            uid = User.objects.get(email=request.POST['email'])
            if uid.password == request.POST['password']:
                request.session['email'] = request.POST['email']

                return render(request,'hotelsindex.html',{'uid':uid})
            else:
                msg = 'Password does not match'
                return render(request,'hotelslogin.html',{'msg':msg})
         except:
            msg = 'Email is not register'
            return render(request,'hotelslogin.html',{'msg':msg})
      else:
        return render(request,'hotelslogin.html')


def hotelsregister(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'User already registered'
            return render(request,'hotelsregister.html',{'msg':msg})
        except:
               request.POST['password'] 
               otp = randrange(1000,9999)
               subject = 'Welcome to Hotel app' 
               message = f"""Hello {request.POST['name']}
               Your Verification OTP is : {otp}.
               """
               email_from = settings.EMAIL_HOST_USER
               recipient_list = [request.POST['email']]
               send_mail( subject, message, email_from, recipient_list )
               global temp
               temp = {
                    'name' : request.POST['name'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password'],
               }
               return render(request,'hotelsotp.html',{'otp':otp}) 

    else:
         return render(request,'hotelsregister.html')  


def hotelsotp(request):
    if request.POST:
        if request.POST['otp']:
            global temp
            User.objects.create(
                name = temp['name'],
                email = temp['email'],
                password = temp['password'],
                address = temp['address'],
                mobile = temp['mobile'],                
            )
            msg = 'User is Created'
            return render(request,'hotelslogin.html',{'msg':msg}) 
        else:
            msg = 'OTP deos not match'
            return render(request,'hotelsotp.html',{'msg':msg,'otp':request.POST['otp']})

    return render(request,'hotelsotp.html')               

def hotelsprofile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.password = request.POST['password']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        
    return render(request,'hotelsprofile.html',{'uid':uid})     


def hotels_fpassword(request):
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
            return render (request,'hotelslogin.html',{'msg':subject})
        except:
            msg = 'User Is Not Registered'
            return render(request,'hotelslogin.html',{'msg':msg})
    return render(request,'hotels_fpassword.html')
            
        
