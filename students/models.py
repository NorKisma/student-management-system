
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
  
 
class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Store the password as a hashed value
    
    def __str__(self):
        return f'Signup: {self.first_name} {self.last_name}'
