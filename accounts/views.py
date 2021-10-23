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
            gettpassword=form.cleaned_data('password1')
            # authenticating the user
            user=authenticate(username=user.username, password=gettpassword)
            # login the user now
            login(request, user)
            return redirect("main:home")
        else:
            form=RegistrationForm()
        return render(request,'accounts/registe.html',{"form":form})        