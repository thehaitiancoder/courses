from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate_course(self, post_data):
        wrong= []
        if len(post_data['name']) < 6:
            wrong.append("The course name needs to be 6 or more characters")
        return wrong

    def add_course(self, cleaned_data):
        return self.create(
            name= cleaned_data['name']
        )

class Course(models.Model):
    name= models.CharField(max_length=255, unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = CourseManager()
    def __unicode__(self):
        return "%s the course" % self.name

class DescriptionManager(models.Manager):
    def validate_course_desc(self, post_data):
        wrong= []
        if len(post_data['description']) < 16:
            wrong.append("The course description needs to be 15 or more characters")
        return wrong

    def add_desc(self, cleaned_data, courseToCreate):
        return self.create(
            content= cleaned_data['description'],
            course= courseToCreate
        )

class Description(models.Model):
    content= models.TextField()
    course= models.OneToOneField(Course, related_name="Description")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= DescriptionManager()
    def __unicode__(self):
        return "%s the Description" % self.course.name
