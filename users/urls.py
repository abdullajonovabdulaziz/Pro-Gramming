from django.contrib import admin
from django.urls import path,include
from .views import signup,login_page,sign_or_log,logoutdef

app_name="users"

urlpatterns = [
    path('', sign_or_log, name="sign_or_log"),
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/',logoutdef,name="log_out")
]