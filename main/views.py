from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# main logic
def home(request):
    return HttpResponse ("<h1>Home Page</h1>")
    