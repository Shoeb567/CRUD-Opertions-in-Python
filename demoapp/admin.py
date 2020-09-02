from django.contrib import admin
from demoapp.models import Student
from demoapp.models import StudentDetails
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentDetails)