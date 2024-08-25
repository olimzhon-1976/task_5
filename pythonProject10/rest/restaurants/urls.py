from django.urls import path
from .views import add_restaurant, restaurant_list
from .views import delete_restaurant
from .views import edit_restaurant

urlpatterns = [
    path('add/', add_restaurant, name='add_restaurant'),
    path('', restaurant_list, name='restaurant_list'),
    path('delete/<int:id>/', delete_restaurant, name='delete_restaurant'),
    path('edit/<int:id>/', edit_restaurant, name='edit_restaurant'),
]

