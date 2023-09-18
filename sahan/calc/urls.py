from django.urls import path

from .import views

urlpatterns =[
    path('home/',views.home,name='home'),#path of what to view
    path('home/add/',views.add,name='add')
]