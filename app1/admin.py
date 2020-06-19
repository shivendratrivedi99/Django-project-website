from django.contrib import admin

# Register your models here.
from .models import Signup
from .models import Login
admin.site.register(Signup)
admin.site.register(Login)