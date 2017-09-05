from django.shortcuts import render, redirect
from .models import Course, Description
from django.contrib import messages

def index(request):
    context= {
        "courses": Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    errors= Course.objects.validate_course(request.POST)
    errors2= Description.objects.validate_course_desc(request.POST)
    if errors or errors2:
        for error in errors:
            messages.error(request, error)
        for error2 in errors2:
            messages.error(request, error2)
    else:
        courseToCreate= Course.objects.add_course(request.POST)
        messages.success(request, "Thanks for adding %s to the list of courses" % courseToCreate.name)

        descToCreate= Description.objects.add_desc(request.POST, courseToCreate)

    return redirect('/courses')

def remove(request, id):

    context= {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)

def destroy(request, id):
    courseToDestroy= Course.objects.get(id=id)
    courseToDestroy.delete()

    return redirect('/')
