from django.contrib import admin
from django.urls import path
from . import views

urlspatterns =[
    path('admin/',admin.site.urls),
    path('signup',views.signup,name='Sign')
]