from django.contrib import admin
from testApp.models import Employee
class EmployeeModel(admin.ModelAdmin):
    list_display=['eno','ename','salary','eaddr']
admin.site.register(Employee,EmployeeModel)
# Register your models here.
