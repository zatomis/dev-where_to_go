from django.urls import path

from places import views

urlpatterns = [
    path('', views.show_main, name='main'),
    path('places/<int:place_id>/', views.get_place_details, name='places'),
    ]
