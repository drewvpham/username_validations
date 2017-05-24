from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def isValid(self, form_data):
        result={'errors':[]}
        if len(form_data['username'])<8 or len(form_data['username'])>16:
            result['errors'].append('Username must be between 8 and 16 characters')
        return result



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

objects = UserManager()
# always required when using a model manager
