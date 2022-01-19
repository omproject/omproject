from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import path

from Hotel.models import Hotel
from .models import *
from random import choices,choice,randrange
from django.conf import settings
from django.core.mail import send_mail



from myapp.models import User

# create your view here

def index(request):
 #   uid = User.objects.get(email=request.session['email'])
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Aview_hotels(request,pk):
    hotel = Hotel.objects.get(id=pk)
    return render(request,'Aview_hotels.html',{'hotel':hotel})    

   

def hotels2(request):
    hotel = Hotel.objects.all()[::-1]
    return render(request,'hotels2.html',{'hotel':hotel}) 

def register(request):
    return render(request,'register.html')

def booking(request):
    return render(request,'booking.html')     

def otp(request):
    return render(request,'otp.html')

def login(request):
    return render(request,'login.html')
    
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




        







