from django.db import models


class User(models.Model):
    user_ID = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    interests = models.CharField(max_length=200)

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    nOfEmployees = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company_interests = models.CharField(max_length=200)