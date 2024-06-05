from django.contrib import admin

from .models import Course,Student


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','department']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name','semester','major','roll_number']
    list_filter = ['major','semester']

