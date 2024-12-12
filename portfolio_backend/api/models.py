from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Create your models here.
