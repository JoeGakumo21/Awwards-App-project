from django.shortcuts import render
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