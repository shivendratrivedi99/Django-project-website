from django.db import models

# Create your models here.
class Profile(models.Model):
    email=models.EmailField(max_length=100,default='a@g.com')
    image=models.ImageField(upload_to='images',default='/media/images/profile.png')
