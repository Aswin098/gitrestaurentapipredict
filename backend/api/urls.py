from django.contrib import admin
from django.urls import path, include
from restaurants.views import RestaurantListView, RestaurantDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Removed registration and token URLs
    path("api/restaurants/", RestaurantListView.as_view(), name="restaurant_list"),
    path("api/restaurants/<int:pk>/", RestaurantDetailView.as_view(), name="restaurant_detail"),
    # Add more URL patterns for restaurant-related functionalities here
]

# Add media URL configuration if needed
