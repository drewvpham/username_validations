from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    print "Inside the index method."
    return render(request, 'username_validations/index.html')


def create(request):
    # print 'inside the create method'
    #Check if user input is valid
    # is_valid = User.objects.validCheck(request.POST)
    # if is_valid:
        user = User.objects.create(username=request.POST['username'])
        message="The username name you entered {} is valid. Thank You!"
        messages.success(request, message.format(user.username))
        return redirect('/success')
    # return redirect('/')

def success(request):
    print "Inside the success method."
    users=User.objects.all().order_by('-id')

    context = {
    "users": users
    }
    print context

    return render(request, 'username_validations/success.html', context)
