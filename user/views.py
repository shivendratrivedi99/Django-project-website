from django.http import HttpResponse
from django.shortcuts import render,redirect
from app1.forms import LoginForm
from app1.models import Signup
from .models import Profile
from .forms import ProfileForm
def user(request):
    if request.method == 'POST':
        return render(request,'user/home.html')
    else:
        return redirect('/auth')
def home(request):
    if(request.COOKIES.get('id')):
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        try:
            obj=Profile.objects.get(email=request.COOKIES.get('id'))
            return render(request,'user/home.html',{'fname':ob.fname,'image':obj.image})
        except:
            return render(request,'user/home.html',{'fname':ob.fname,'image':'/images/profile.png'})
    else:
        return redirect('/auth/signin')
def about(request):
    if(request.COOKIES.get('id')):
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        try:
            obj=Profile.objects.get(email=request.COOKIES.get('id'))
            return render(request,'user/about.html',{'fname':ob.fname,'image':obj.image})
        except:
            return render(request,'user/about.html',{'fname':ob.fname,'image':'/images/profile.png'})
    else:
        return redirect('/auth/signin')
    return render(request,'user/about.html')
def contactus(request):
    if(request.COOKIES.get('id')):
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        try:
            obj=Profile.objects.get(email=request.COOKIES.get('id'))
            return render(request,'user/contactus.html',{'fname':ob.fname,'image':obj.image})
        except:
            return render(request,'user/contactus.html',{'fname':ob.fname,'image':'/images/profile.png'})
    else:
        return redirect('/auth/signin')

def profile(request):
    if(request.COOKIES.get('id')):
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        try:
            obj=Profile.objects.get(email=request.COOKIES.get('id'))
            form=ProfileForm(instance=obj)
            return render(request,'user/profile.html',{'fname':ob.fname,'form':form,'email':ob.email,'image':obj.image})
        except:
            form=ProfileForm()
            return render(request,'user/profile.html',{'fname':ob.fname,'form':form,'email':ob.email,'image':'/images/profile.png'})
    else:
        return redirect('/auth/signin')

def upload(request):
    if(request.COOKIES.get('id')):
        if request.method=='POST':
            try:
                obj=Profile.objects.get(email=request.COOKIES.get('id'))
                form=ProfileForm(request.POST,request.FILES,instance=obj)
                ob=Signup.objects.get(email=request.COOKIES.get('id'))
                if form.is_valid():
                    form.save()
                    return redirect('/user/profile')
            except:
                form=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('/user/profile')
        else:
            form=ProfileForm()
            return render(request,'user/profile.html',{'form':form})

    else:
        return redirect('/auth/signin')
def websites(request):
    if(request.COOKIES.get('id')):
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        try:
            obj=Profile.objects.get(email=request.COOKIES.get('id'))
            return render(request,'user/websites.html',{'fname':ob.fname,'image':obj.image})
        except:
            return render(request,'user/websites.html',{'fname':ob.fname,'image':'/images/profile.png'})
    else:
        return redirect('/auth/signin')
        
def logout(request):
    form=LoginForm()
    response=render(request,'app1/signin.html',{'form':form,'status':1})
    response.delete_cookie('id')
    # try:
    #   del request.session['id']
    # except:
    #     pass
    return response