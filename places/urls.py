from django.urls import path

from places import views

urlpatterns = [
    path('', views.show_main, name='main'),
    ]
