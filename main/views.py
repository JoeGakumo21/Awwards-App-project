from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
# main logic
def home(request):
    # accessing all details from the database created on models files
    allAwardsDetails=Award.objects.all()

    context={"awards":allAwardsDetails}
    return render (request, 'main/index.html', context)
# another logic to access all details 
def detail(request, id):
    projects=Award.objects.get(id=id)
    context={"project":projects}
    return render(request,'main/details.html',context)


 #add new projects to database  and post it
def  add_project(request):
    if request.method=="POST":
        form=UploadProjectForm(request.POST or None)


        # checking if the form is valid
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect ("main:home")
    else:
        form=UploadProjectForm()
    return render(request, "main/addproject.html",{"form":form})            

# editing individaul project details
def edit_project(request, id):
    # getting the project linked id
    individualproject=Award.objects.get(id=id)
# checking the form
    if request.method=="POST":
        form=UploadProjectForm(request.POST or None, instance=individualproject)
# check if form is valid
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect("main:detail",id)
    else:
        form=UploadProjectForm(instance=individualproject)
    return render(request,'main/addproject.html',{"form":form})    