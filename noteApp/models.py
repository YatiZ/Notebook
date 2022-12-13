from django.db import models
import uuid


# Create your models here.
class Page(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add= True)
    title= models.CharField(max_length= 100)
    page = models.TextField(max_length = 5000)
    image = models.ImageField(upload_to='images',blank = True)


    def __str__(self):
        return self.title
    def __str__(self):
        return str(self.date)

class Todolist(models.Model):
    text = models.TextField(max_length=1000)
    datetodo = models.DateField()
    

class Image(models.Model):
    caption = models.CharField(max_length=200,blank=True)
    image = models.FileField(upload_to='images')

class Book(models.Model):
    cover = models.ImageField(upload_to='cover')
    pdf = models.FileField(upload_to='pdf')


class newstats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    android = models.IntegerField()
    iph = models.IntegerField(default=True)
    oth = models.IntegerField(default=True)

   