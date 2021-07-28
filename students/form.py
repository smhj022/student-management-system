from django import forms

from students.constants import CLASSES_CHOICE_LIST, GENDER_CHOICES_LIST


class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=30)
    standard = forms.CharField(label="Standard", widget=forms.Select(choices=CLASSES_CHOICE_LIST))
    gender = forms.CharField(label="Gender", widget=forms.Select(choices=GENDER_CHOICES_LIST))
    city = forms.CharField(max_length=30)
