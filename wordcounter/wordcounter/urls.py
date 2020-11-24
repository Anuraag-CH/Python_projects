
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="h"),
    path('count',views.count,name="c"),
    path('about',views.about,name="a"),

]
