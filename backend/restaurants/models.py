from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    best_meal = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
