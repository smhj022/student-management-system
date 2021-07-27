from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    standard = models.IntegerField()
    roll_no = models.AutoField(primary_key=True)
    male = models.CharField(max_length=1)
    city = models.CharField(max_length=30)
    new_student = models.BooleanField()
