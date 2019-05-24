import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbv.settings')
import django
django.setup()
from testApp.models import *
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(2000,3000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,salary=fesal,eaddr=feaddr)
populate(20)
