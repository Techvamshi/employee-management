from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee


def dashboard(request):
    return render(request, "dashboard.html", {
        "total_employees": Employee.objects.count(),
        "total_departments": Department.objects.count(),
        "recent_employees": Employee.objects.select_related("department").order_by("-id")[:5],
    })


def employee_list(request):
    employees = Employee.objects.select_related("department")
    return render(request, "employee_list.html", {"employees": employees})


def employee_detail(request, pk):
    return render(request, "employee_detail.html", {"employee": get_object_or_404(Employee, pk=pk)})


def employee_add(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        employee = form.save()
        return redirect("employee_detail", pk=employee.pk)
    return render(request, "employee_form.html", {"form": form, "title": "Add employee"})


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("employee_detail", pk=employee.pk)
    return render(request, "employee_form.html", {"form": form, "title": "Edit employee"})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request, "employee_confirm_delete.html", {"employee": employee})


def department_list(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("department_list")
    departments = Department.objects.annotate(employee_count=Count("employees"))
    return render(request, "department_list.html", {"form": form, "departments": departments})
