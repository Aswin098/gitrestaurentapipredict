from django.shortcuts import render
from .models import Restaurant
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RestaurantSerializer

# Restaurant management views
class RestaurantListView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Restaurant.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDeleteView(generics.DestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Restaurant.objects.filter(owner=user)
