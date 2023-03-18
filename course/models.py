
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    

    class Meta:
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.title


class Course(models.Model):
    user = models.ForeignKey(User, related_name="course", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="course", on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return self.course_name
