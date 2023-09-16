from django.urls import path

from .import views

urlpatterns =[
    path('',views.home,name='home'),#path of what to view
    path('add',views.add,name='add')
]