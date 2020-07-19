from django.shortcuts import render, redirect
from .models import User


# Create your views here.

def index(request):
  context = {
    'users': User.objects.all()
  }
  
  return render(request, 'index.html', context)

def sign_up(request):
  print(request.POST)
  # retrieve data from form
  # add a User to dashboard
  # redirect the form to the index page
  User.objects.create(
    first_name= request.POST['first_name'],
    last_name= request.POST['last_name'],
    email_address= request.POST['email'],
    age= request.POST['age'],
  )
  
  return redirect('/')
