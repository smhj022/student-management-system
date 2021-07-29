from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View

from students.constants import CLASSES_CHOICE_LIST

from .form import StudentRegistration
from .models import Student

# Create your views here.


def roll_no_generator(standard):
    students = Student.objects.filter(standard=standard)
    students_in_class = len(students)
    try:
        last_student_roll_no = students[students_in_class-1].roll_no
        last_value_of_roll_no = int(last_student_roll_no[-1])
    except AssertionError:
        last_value_of_roll_no = 0

    if len(standard) == 4:
        roll_prefix = standard[:2]
    else:
        roll_prefix = standard[0]
    roll_suffix = str(last_value_of_roll_no+1)
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
            student_roll_no = roll_no_generator(student_standard)

            # add student to database
            new_student = Student(name=student_name, standard=student_standard,
                                  roll_no=student_roll_no, gender=student_gender, city=student_city)
            new_student.save()
            return HttpResponseRedirect("/")

        return render(request, "students/registration.html", {
            "form": form
        })


class ClassDetails(View):
    def get(self, request, standard):
        students_in_class = Student.objects.filter(standard=standard)
        return render(request, "students/class_details.html", {
            "students_in_class": students_in_class,
            "standard": standard
        })


class StudentDetails(View):
    def get(self, request, id):
        form = StudentRegistration()
        student_detail = Student.objects.get(id=id)
        return render(request, "students/student_detail.html", {
            "student_detail": student_detail,
            "form": form
        })

    def post(self, request, id):
        req_body_params = request.POST
        try:
            student_detail: Student = Student.objects.get(id=id)
            student_detail.name = req_body_params["name"]
            student_detail.standard = req_body_params["standard"]
            student_detail.gender = req_body_params["gender"]
            student_detail.city = req_body_params["city"]
            student_detail.roll_no = roll_no_generator(req_body_params["standard"])
            student_detail.save()
            return HttpResponseRedirect("/")

        except Student.DoesNotExist:
            return HttpResponseRedirect("/")


        
