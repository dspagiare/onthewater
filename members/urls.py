from django.urls import path

from . import views


urlpatterns = [
    path("", views.testPage, name="testPage"),
]