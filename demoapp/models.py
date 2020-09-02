from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	number=models.CharField(max_length=20)
	def __str__(self):
		return self.name

class StudentDetails(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	def __str__(self):
		return self.username