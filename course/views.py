from django.shortcuts import render , get_object_or_404
from . models import Category
from . models import Course

# Create your views here.
def course_detail(request,category_slug,slug):
    course  = get_object_or_404(Course, slug = slug)
    return render(request, "course_detail.html", {'course':course})
 
def category_detail(request, slug):
    category = get_object_or_404(Category, slug = slug)
    courses = category.course.all()
    context={
        "category": category,
        "courses": courses
    }
    return render (request, "category_detail.html", context)