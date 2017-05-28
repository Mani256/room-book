from django.shortcuts import render

# Create your views here.
def home(request):
    home_context = {'message':'Welcome to our website'}
    return render(request,'home.html',home_context)