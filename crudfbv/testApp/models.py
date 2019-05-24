from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    salary=models.FloatField()
    eaddr=models.CharField(max_length=30)
# Create your models here.
