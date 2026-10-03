from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
