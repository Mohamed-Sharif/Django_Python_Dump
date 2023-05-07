from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name
