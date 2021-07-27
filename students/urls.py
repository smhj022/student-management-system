from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index-page"),
    path("registration", views.StudentEntry.as_view(), name="registration-page")
]
