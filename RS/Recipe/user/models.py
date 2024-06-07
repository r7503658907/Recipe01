from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.admin import User
import datetime

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Customer(models.Model):
    cSid = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()

class Category(models.Model):
    CategoryName = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.CategoryName
class Recipe(models.Model):
    RecipeId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()
    serving_size = models.PositiveIntegerField()
    CategoryName = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title
class Review(models.Model):
    RecipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


class Rating(models.Model):
    RatingId = models.AutoField(primary_key=True)
    RecipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


class Review(models.Model):
    ReviewId = models.AutoField(primary_key=True)
    RecipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
