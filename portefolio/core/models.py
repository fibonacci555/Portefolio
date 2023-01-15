from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null = True)
    email = models.EmailField(blank=True, null = True)
    body = models.TextField(blank=True, null = True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(f"{self.name} - {self.date}")

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null = False, default="project")
    subname = models.CharField(max_length=100, blank=False, null = False, default="project-sub")
    body = models.TextField(blank=True, null = True)
    pic = models.ImageField(blank=False, null=False, upload_to='uploads')
    github = models.URLField(blank=False, null=False)
    link = models.URLField(blank=True, null=True)

   
