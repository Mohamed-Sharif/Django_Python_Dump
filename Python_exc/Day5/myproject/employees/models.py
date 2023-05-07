from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='employees/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
