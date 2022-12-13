from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('schedule/',views.schedule,name='schedule'),
    path('addpage/',views.addpage,name='addpage'),
    path('addphoto/',views.addphoto,name = 'addphoto'),
    path('name/',views.get_name,name='get_name'),
    path('image/',views.image,name='image'),
    path('book/',views.book,name='book'),
    path('ssession/',views.setsession),
    path('gesession/',views.getsession),
   
]