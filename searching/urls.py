from django.urls import path
from . import views

urlpatterns = [
    path("", views.fetchdata, name="fetchdata"),
    path("data", views.searching, name="data"),
]
