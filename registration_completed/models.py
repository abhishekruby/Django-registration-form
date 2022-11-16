from django.db import models
from django import forms

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

DEGREE_CHOICES = (
    ('bca','BCA'),
    ('b-tech', 'B-Tech'),
    ('bsc','BSC'),
)

class Form(models.Model):
    image = models.ImageField(upload_to="students_Photo/")
    first_name = models.CharField(max_length=120);
    last_name = models.CharField(max_length=120);
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=120,choices=GENDER_CHOICES);
    degree = models.CharField(max_length=120,choices=DEGREE_CHOICES);
    email = models.EmailField();
    number = models.CharField(max_length=120);
    description = models.TextField();


    def __str__(self):
        return str(self.id)