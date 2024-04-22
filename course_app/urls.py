from django.contrib import admin
from django.urls import path
from .views import home,lesson,account_def

app_name='course_app'

urlpatterns=[
    path("",home, name='home'),
    path("lesson/<str:title>", lesson, name='lesson'),
    path("account", account_def, name='account')
]
