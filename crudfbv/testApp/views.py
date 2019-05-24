from django.shortcuts import render,redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm

def retrive_view(request):
    employee=Employee.objects.all()
    return render(request,'testApp/index.html',{'employee':employee})
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    return render(request,'testApp/create.html',{'form':form})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid:
            form.save()
            return redirect('/')

    return render(request,'testApp/update.html',{'employee':employee})


# Create your views here.
