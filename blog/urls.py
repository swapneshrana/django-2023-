from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    #localhost:8000/blog/index
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('feedback/',views.feedback)
    
]