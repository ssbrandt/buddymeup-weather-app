from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
]
