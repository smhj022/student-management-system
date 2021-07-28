from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.views import View
from .form import StudentRegistration
from .models import Student


# Create your views here.

def roll_no_generator(no_of_Student_in_class, standard):
    pass


def index(request):
    return render(request, "students/index.html")


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
            new_student_standard = (data["standard"])
            student = Student.objects.filter(standard=new_student_standard)
            print(student)
            return HttpResponseRedirect("/")

        return render(request, "students/registration.html", {
            "form": form
        })
