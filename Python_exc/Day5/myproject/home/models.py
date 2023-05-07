from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField()

    def __str__(self):
        return self.title