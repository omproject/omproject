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

