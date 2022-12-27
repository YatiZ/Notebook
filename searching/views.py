from django.shortcuts import render
from django.http import HttpResponse
from .models import carsdata
from django.contrib import messages

# Create your views here.


def fetchdata(request):
    data = carsdata.objects.all()
    return render(request, "fetchdata.html", {"data": data})


def searching(request):
    result = []
    if "q" in request.GET:
        data = request.GET["q"]

        result = carsdata.objects.filter(first_name__icontains=data)

    return render(request, "search.html", {"result": result})
