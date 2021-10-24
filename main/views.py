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
    reviews=Review.objects.filter(project=id).order_by("comment")
    context={"project":projects, "reviews":reviews}
    return render(request,'main/details.html',context)


 #add new projects to database  and post it
def  add_project(request):

# adding functionality who to add movie
    if request.user.is_authenticated:
       
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

    return redirect("accounts:login")
# editing individaul project details
def edit_project(request, id):
    if request.user.is_authenticated:
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
    return redirect("accounts:login")

# function for deleting the project
def deleteproject(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
        
            projectname=Award.objects.get(id=id)
            projectname.delete()
            return redirect("main:home")
        else:
            return redirect("main:home")
    return redirect("accounts:login")


# function to commit comments and rating
def add_review(request, id):
    if request.user.is_authenticated:
        project=Award.objects.get(id=id)
        if request.method == "POST":
            form=ReviewForm(request.POST or None)
            if form.is_valid():
                data=form.save(commit=False)
                data.comment=request.POST["comment"]
                data.rating=request.POST["rating"]
                data.user=request.user
                data.project=project
                data.save()
                return redirect("main:detail", id)
        else:
            form=ReviewForm()  
        return render(request,'main/details.html', {"form":form})
    else:
        return redirect("accounts:login")              

 #logic to delete a comment
def edit_review(request, project_id, review_id):
    if request.user.is_authenticated:
        project=Award.objects.get(id=project_id)
        review=Review.objects.get(project=project, id=review_id)

        # check if the review was done by looged in user
        if request.user == review.user:
            # grant user to review
            if request.method== "POST":
                form=ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data= form.save(commit=False)
                    data.save()
                    return redirect("main:detail", project_id) 
            else:
                form=ReviewForm(instance=review)
            return render(request,'main/editreview.html', {"form":form})
        else:
         return redirect("accounts:login")                
# delete review
def delete_review(request, project_id, review_id):
    if request.user.is_authenticated:
        project=Award.objects.get(id=project_id)
        review=Review.objects.get(project=project, id=review_id)

        # check if the review was done by looged in user
        if request.user == review.user:
            # grant user to review
           review.delete()
        return redirect("main:detail", project_id)
       
    else:
        return redirect("accounts:login")                


