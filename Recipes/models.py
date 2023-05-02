from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class APIData(models.Model):
    recipe_name = models.CharField(max_length=200),
    recipe_img = models.CharField(max_length=10000),
    recipe_ing = models.CharField(max_length=10000)


class Guest(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.username



class Recipe(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1800, null=True)
    note = models.IntegerField()





