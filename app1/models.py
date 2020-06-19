from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Signup(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    password=models.CharField(max_length=100)
    agree = models.BooleanField(default=False)

class Login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)