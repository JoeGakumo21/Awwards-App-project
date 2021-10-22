from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# main logic
def home(request):
    # accessing all details from the database created on models files
    allAwardsDetails=Award.objects.all()
    return render (request, 'main/index.html')
  