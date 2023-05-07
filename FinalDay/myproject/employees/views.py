from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
def employee_list(request):
    count=0
    employees = Employee.objects.all()
    print("The list" + str(count))
    count +=1
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    count=0
    print("Details" + str(count))
    count +=1
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee=form.save()
            print(employee.first_name, employee.last_name, employee.department)
            return redirect('employees:employee_list')
        else:
            print(form.errors)
    else:
        form = EmployeeForm()
    context = {'form': form}
    return render(request, 'employees/employee_form.html', context)

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    context = {'form': form}
    return render(request, 'employees/employee_form.html', context)

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee_list')
    context = {'employee': employee}
    return render(request, 'employees/employee_confirm_delete.html', context)
