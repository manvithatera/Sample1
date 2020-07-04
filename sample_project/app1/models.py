from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    designation =models.CharField(max_length=50)
    salary =models.DecimalField(decimal_places=2,max_digits=1000)
    address = models.TextField(max_length=500,blank=True,null=True)
    company = models.CharField(max_length=60,blank=False,null=False)
