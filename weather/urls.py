from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:city_id>/', views.delete_city, name='delete_city'),
    path('delete_all/', views.delete_all_cities, name='delete_all_cities'),
]
