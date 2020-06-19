from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import SignupForm
from . forms import LoginForm
from .models import Login
from . models import Signup
from user.views import user
def auth(request):
    return redirect('/auth/signin')

# def login(request):
#     form=LoginForm()
#     return render(request,'app1/signin.html',{'form':form})
def signin(request):
    if(request.COOKIES.get('id')):
    # if request.session.has_key('id'):
    #     id=request.session['id']
        
        ob=Signup.objects.get(email=request.COOKIES.get('id'))
        return render(request,'user/home.html',{'fname':ob.fname})
    else:
        status=1   
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                e=request.POST.get("email")
                p=request.POST.get("password")
                response=HttpResponse()
                try:
                    print("hellooodijfisdjfisjfij")
                    ob=Signup.objects.get(email=e,password=p)
                    print("hellooodijfisdjfisjfij")
                    if ob.email==e and ob.password==p:
                        ob=Signup.objects.get(email=e)
                        response=render(request,'user/home.html',{'fname':ob.fname,'image':'/images/profile.png'})
                        response.set_cookie("id",e,max_age=10000)
                        # request.session['id'] = e
                        # status=1
                        return response
                except:
                    status=0
                    return render(request,'app1/signin.html',{'form':form,'status':status})
        else:
            form=LoginForm()
            return render(request,'app1/signin.html',{'form':form,'status':status})
def signup(request):
    form=SignupForm()
    return render(request,'app1/signup.html',{'form':form})
def insert(request):
    if request.method=='POST':
        #form=SignupForm(request.POST,request.FILES)
        form=SignupForm(request.POST)
        if form.is_valid():
            try:
                if Signup.objects.filter(email=request.POST.get("email")):
                    status=1
                    return render(request,'app1/signup.html',{'form':form,'status':status})
                else:
                    form.save()
                    return redirect('/auth/show')
            except:
                form.save()
                return redirect('/user')
    else:
        form=SignupForm()
        return render(request,'app1/signup.html',{'form':form})

def show(request):
    #ob=Employee.objects.all()
    #select data from table
    ob=Signup.objects.order_by('-id')#-for descending
    # ob=Employee.objects.filter(name="ankul")
    #ob=Employee.objects.filter(name="ankul",email="cetpa@gmail.com")
    return render(request,'app1/show.html',{'signup':ob})
    # return redirect('/user')