from django.urls import path
from . import views

urlpatterns = [
    path("restaurants/", views.RestaurantListView.as_view(), name="restaurant-list"),  # Endpoint for listing restaurants
    path("restaurants/delete/<int:pk>/", views.RestaurantDeleteView.as_view(), name="delete-restaurant"),  # Endpoint for deleting restaurants
]
