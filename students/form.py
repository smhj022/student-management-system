from django import forms

class_choice = [
    ("LKG", "LKG"),
    ("UKG", "UKG"),
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    ("9th", "9th"),
    ("10th",  "10th")
]
gender = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]


class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=30)
    standard = forms.CharField(label="Standard", widget=forms.Select(choices=class_choice))
    gender = forms.CharField(label="Gender", widget=forms.Select(choices=gender))
    city = forms.CharField(max_length=30)
