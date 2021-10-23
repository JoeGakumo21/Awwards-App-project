from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# creating the logic here for accounts registration
def register(request):
    if request.method=="POST":
        form =RegistrationForm(request.POST or None)


        # check if the form is valid
        if form.is_valid():
            user=form.save()


            # get the password
            gettpassword=form.cleaned_data.get('password1')
            # authenticating the user
            user=authenticate(username=user.username, password=gettpassword)
            # login the user now
            login(request, user)
            return redirect("accounts:login")
    else:
        form=RegistrationForm()
    return render(request,"accounts/register.html", {"form":form})

# login function
def login_user(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']


        # check the credential
        user=authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("main:home")
            else:
                return render(request, "accounts/login.html",{"error":"Your account has been disabled."})
        else:
            return render(request,"accounts/login.html",{"error":"Invalid Username or Password. Try Again or Check Your credentials."})   
    return render(request, "accounts/login.html")                 


