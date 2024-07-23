from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city_name = models.CharField(max_length=200)
    zipcode   = models.CharField(max_length=200)
    state     = models.CharField(max_length=200)
    member_since = models.DateTimeField("date joined")