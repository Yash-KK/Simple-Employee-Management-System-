# from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField()
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
       return f"{self.first_name} ({self.phone})"