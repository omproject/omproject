from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    address = models.TextField(null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    pic = models.FileField(upload_to='Profile pic',default='avtar.png')
    
    def __str__(self):
        return self.name

class Hotel(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=50)
    hotel_adderss = models.TextField()
    hotel_country = models.CharField(max_length=20,default="india")
    hotel_rooms = models.IntegerField()
    hotel_mobile = models.CharField(max_length=20)
    hotel_price = models.IntegerField(default=0)
    hotel_wifi = models.BooleanField()
    hotel_photos = models.FileField(upload_to='hotel pic',null=True,blank=True)
    add_details = models.TextField()
    hotel_acroom = models.CharField(max_length=30)

    def __str__(self):
        return self.hotel_name

