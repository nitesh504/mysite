
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Welcome")
    return render(request,'index.html')
def about(request):
    return HttpResponse("Welcome to About page")
def contact(request):
    return HttpResponse("Welcome to Contact page")

