from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def validCheck(self, form_data):
        print "Inside isValid method."
        valid=True
        if len(form_data['username'])<8 or len(form_data['username'])>16:
            messages.error(request, "Username is required.")
            valid=False
        return valid

class User(models.Model):
    username = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = UserManager()
# always required when using a model manager
