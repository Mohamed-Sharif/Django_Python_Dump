from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})
