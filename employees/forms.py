from django import forms
from .models import Department, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_id", "name", "email", "phone", "department",
                  "designation", "salary", "joining_date"]
        widgets = {"joining_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")}
