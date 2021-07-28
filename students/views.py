from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

from students.constants import CLASSES_CHOICE_LIST

from .form import StudentRegistration
from .models import Student

# CLASSES_IN_SCHOOL = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
# Create your views here.


def roll_no_generator(no_of_Student_in_class, standard):
    if len(standard) == 4:
        roll_prefix = standard[:2]
        print(type(roll_prefix))
        print(roll_prefix)
    else:
        roll_prefix = standard[0]
    roll_suffix = str(no_of_Student_in_class+1)
    print(roll_suffix)
    roll_no = roll_prefix + "0" + roll_suffix
    return roll_no


def index(request):
    return render(request, "students/index.html", {"CLASSES_CHOICE_LIST": CLASSES_CHOICE_LIST})


class StudentEntry(View):
    def get(self, request):
        form = StudentRegistration()
        return render(request, "students/registration.html", {
            "form": form
        })

    def post(self, request):
        form = StudentRegistration(request.POST)

        if form.is_valid:
            data = request.POST
            student_name = data["name"]
            student_gender = data["gender"]
            student_city = data["city"]
            student_standard = data["standard"]

            # generating roll no
            students = Student.objects.filter(standard=student_standard)
            students_in_class = len(students)
            student_roll_no = roll_no_generator(students_in_class, student_standard)

            # add student to database
            new_student = Student(name=student_name, standard=student_standard,
                                  roll_no=student_roll_no, gender=student_gender, city=student_city)
            new_student.save()
            return HttpResponseRedirect("/")

        return render(request, "students/registration.html", {
            "form": form
        })
