from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("registration", views.StudentEntry.as_view(), name="registration-page"),
    path("class-detail/<str:standard>", views.ClassDetails.as_view(), name="class-details")
]
