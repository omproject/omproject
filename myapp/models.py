from re import U
from turtle import title
from django.db import models
from Hotel.models import Hotel

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


class bookingUser(models.Model):

    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    hname = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    no_person = models.IntegerField()
    bookprice = models.IntegerField(default=0)
    

    def __str__(self):
        return self.uid.fname + '' + self.hname.hotel_name  

     
    