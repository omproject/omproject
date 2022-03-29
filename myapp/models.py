from enum import _auto_null
from re import U
from sqlite3 import Date
from turtle import title
from django.db import models
from pytz import timezone
from Hotel.models import Hotel
import uuid

# Create your models here.

class User(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=50)
    

    def __str__(self):
        return self.fname + ' ' + self.lname


class BookingUser(models.Model):

    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    hname = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    no_person = models.IntegerField()
    bookprice = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    booking_id = models.UUIDField(editable = False,unique=True,default=uuid.uuid4)
    pay_id = models.CharField(max_length=50,null=True,blank=True)
    cancel_payment = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)

    def __str__(self):
        return self.uid.fname + '' + self.hname.hotel_name  

     
    