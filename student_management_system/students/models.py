#from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=120,null=False,unique=True)
    course_number = models.PositiveIntegerField(db_index=True,default=1)
    department = models.CharField(max_length=200,default='CS')
    course_credits = models.IntegerField()
    num_lectures = models.PositiveIntegerField()
    instructor_name = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='Instructor')

    def __str__(self):
        return self.course_name

class Prerequisites(models.Model):
    course_name = models.ForeignKey(to=Course,on_delete=models.CASCADE,related_name='selected_course')
    prerequisites=models.ForeignKey(to=Course,related_name='Courses_Required',null=True,blank=True,on_delete=models.CASCADE)
class Student(models.Model):
    student_name=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='Student_Name')
    roll_number = models.CharField(max_length=20)
    semester = models.CharField(max_length=2)
    major = models.CharField(max_length=2)

    courses_enrolled = models.ForeignKey(to=Course,related_name='enrolled_courses',on_delete=models.CASCADE)

    class Meta:
        ordering = ['roll_number','semester']
    def __str__(self):
        return self.student_name

