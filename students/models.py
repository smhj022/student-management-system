from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    standard = models.IntegerField()
    roll_no = models.CharField(max_length=5)
    gender = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    # new_student = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name} ({self.standard})"
