from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class_choice = ["LKG", "UKG", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]
gender = ["Male", "Female", "Other"]


class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=30)
    standard = forms.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    gender = forms.CharField(max_length=5)
    city = forms.CharField(max_length=30)
