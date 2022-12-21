from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .forms import NameForm
from .models import Page, Todolist, Image, Book
from django.http import HttpResponse
import requests
from .models import newstats
from django.db.models import F

# Create your views here.


def index(request):
    return render(request, "index.html")


def home(request):
    images = Image.objects.all()
    post = Page.objects.all()
    books = Book.objects.all()
    return render(request, "home.html", {"post": post, "images": images, "book": books})


# def home(request):
#     return render(request,'home.html')


def schedule(request):
    return render(request, "schedule.html")


def addpage(request):
    if request.method == "POST":
        title = request.POST["title"]
        page = request.POST["page"]
        photo = request.FILES.get("photo")
        # return HttpResponse(photo)
        if photo == None:
            post = Page.objects.create(title=title, page=page)
            post.save()
        else:
            post = Page.objects.create(title=title, page=page, image=photo)
            post.save()
        return redirect("home")
    return render(request, "addpage.html")


def addphoto(request):
    return redirect("home")


def todolist(request):
    if request.method == "POST":
        text = request.POST["text"]
        date = request.POST["date"]
        lists = Todolist.objects.create(text=text, datetodo=date)
        lists
    return render(request, "list.html")


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return redirect("home")
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})


# def image(request):
#     form = ImageForm()
#     if request.method == 'POST':
#         form = ImageForm(request.POST)
#         images = request.FILES.getlist('image')
#         image_list = []
#         if form.is_valid():
#             project = form.save()
#             for image in images:
#                 new_img=Image(project = project,image = image).save()
#                 image_list.append(new_img.image.url)
#         return render(request,'image.html',{'urls':image_list})

#     return render(request,'image.html')

# def multi_img(request):
#     if request.method == 'POST':
#         files = request.FILES.getlist('image')
#         for file in files:
#             new_file = Image(image = image)
#             new_file.save()
#         return redirect('home')


def image(request):
    # images = Image.objects.all()
    # post = Page.objects.all()
    if request.method == "POST":
        caption = request.POST["caption"]
        images = request.FILES.getlist("image")
        image_list = []

        for image in images:
            new_img = Image(caption=caption, image=image)
            new_img.save()
            image_list.append(new_img.image.url)
        # return render(request,'home.html',{'img_urls':image_list})
        # return render(request,'home.html',{'img_urls':image_list,'images':images,'new_img':new_img})
        return redirect("home")

    return render(request, "image.html")


def book(request):
    books = Book.objects.all()
    if request.method == "POST":
        cover_pic = request.FILES.get("cover")
        pdf_file = request.FILES.get("pdf")
        book = Book.objects.create(cover=cover_pic, pdf=pdf_file)
        book.save()
        return redirect("book")
    return render(request, "book.html", {"books": books})


def setsession(request):
    request.session["sname"] = "Yati"
    request.session["semail"] = "zuzu62113@gmail.com"
    return HttpResponse("session is set")


def getsession(request):

    student_name = request.session["sname"]
    student_email = request.session["semail"]
    return HttpResponse(student_name + " " + student_email)


class DemoMIddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def stats(self, os_info):
        if "Windows" in os_info:
            newstats.objects.all().update(win=F("win") + 1)
        elif "mac" in os_info:
            newstats.oblects.all().update(mac=F("mac" + 1))
        elif "android" in os_info:
            newstats.objects.all().update(android=F("android" + 1))
        elif "iph" in os_info:
            newstats.objects.all().update(iph=F("iph" + 1))
        else:
            newstats.objects.all().update(oth=F("oth" + 1))

    def __call__(self, request):

        if "admin" not in request.path:
            self.stats(request.META["HTTP_USER_AGENT"])

        response = self.get_response(request)
        return response
