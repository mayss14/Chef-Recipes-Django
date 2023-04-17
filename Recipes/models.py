from django.db import models

# Create your models here.


class APIData(models.Model):
    recipe_name = models.CharField(max_length=200),
    recipe_img = models.CharField(max_length=10000),
    recipe_ing = models.CharField(max_length=10000)

