from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Page(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    page = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return str(self.date)


class Todolist(models.Model):
    text = models.TextField(max_length=1000)
    datetodo = models.DateField()


class Image(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to="images")


class Book(models.Model):
    cover = models.ImageField(upload_to="cover")
    pdf = models.FileField(upload_to="pdf")


class newstats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    android = models.IntegerField()
    iph = models.IntegerField(default=True)
    oth = models.IntegerField(default=True)


# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN",'Admin'
#         STUDENT = "STUDENT",'Student'
#         TEACHER = "TEACHER",'Teacher'

#     base_role = Role.ADMIN

#     role = models.CharField(max_length=50, choices=Role.choices)

#     def save(self, *args , **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)

# class Student(User):
#     base_role = User.Role.STUDENT

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "Only For Students"
