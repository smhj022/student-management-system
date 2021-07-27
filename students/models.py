from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    standard = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    roll_no = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    new_student = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name} ({self.standard})"