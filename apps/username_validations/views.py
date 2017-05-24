from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'username_validations/index.html')
    pass

def create(request):
    print 'inside the create method'
    print request.POST
    is_valid = User.objects.isValid(request.POST)
    if is_valid['errors']:
        messages.error(request, is_valid['errors'])

    User.objects.create(username=request.POST['username'])
    users=User.objects.all()
    context = {
    "users": User.objects.all()
    # select * from Blog
    }
    return render(request, 'username_validations/success.html')

def success(request):

    return render(request, 'username_validations/success.html')
