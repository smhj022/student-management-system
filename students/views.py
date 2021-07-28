from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from .form import StudentRegistration
from django.views import View

# Create your views here.


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
            print(data["standard"])
            return HttpResponseRedirect("/")

        return render(request, "students/registration.html", {
            "form": form
        })
