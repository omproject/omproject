from re import U
from django.db import models

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
    name = models.CharField(max_length=50)
    check_in = models.DateField()
    check_out = models.DateField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)


    def __str__(self):
        return self.name + ''

     
    