import datetime

from django.db import models


# Create your models here.

GENDER_CHOICES = (
    ('', 'Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

DEGREE_CHOICES = (
    ('','select'),
    ('bca','BCA'),
    ('b-tech', 'B-Tech'),
    ('bsc','BSC'),
    ('other','OTHER'),
)
class Form(models.Model):
    first_name = models.CharField(max_length=120);
    last_name = models.CharField(max_length=120);
    date_of_birth = models.DateField(default=datetime.date.today())
    gender = models.CharField(max_length=120,choices=GENDER_CHOICES);
    degree = models.CharField(max_length=120,choices=DEGREE_CHOICES);
    email = models.EmailField();
    number = models.CharField(max_length=120);
    description = models.TextField();
    def __str__(self):
        return str(self.id)