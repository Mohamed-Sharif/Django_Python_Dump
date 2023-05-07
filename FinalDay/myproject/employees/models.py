from django.db import models
from departments.models import Department

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='employees/Media')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
