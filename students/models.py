from django.db import models

# Create your models here.
# Object Relational Mapper (ORM)


class Student(models.Model):
    name = models.CharField(max_length=30)
    standard = models.CharField(max_length=4)
    roll_no = models.CharField(max_length=5)
    gender = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name} ({self.standard}, {self.roll_no})"
