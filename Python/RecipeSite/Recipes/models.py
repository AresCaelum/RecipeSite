import uuid
from django.db import models


# Create your models here.
class User(models.model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid64, editable=False)
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=100)


class Recipe(models.model):
    recipe_id = models.UUIDField(primary_key=True, default=uuid.uuid64, editable=False)
    recipe_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)          # Every-time someone votes this value will increase
    vote_rating = models.IntegerField(default=0)    # our voting will allow ratings of integer values 1 - 5
    user_id = models.CharField(max_length=36, primary_key=True)


class Votes(models.model):
    # Everytime you vote we will create an entry for what you voted for
    # and what you rated it, if you come to a recipe you already rated
    # we will load your rating, so if you change it it will just change
    # what you previously rated it
    user_id = models.CharField(max_length=36, primary_key=True)
    recipe_id = models.CharField(max_length=36)
    rating = models.IntegerField(default=1)


class MeasurementTypes(models.model):
    measurement_type = models.IntegerField(default=0)
    char_field = models.CharField(max_length=100)


class Ingredient(models.model):
    ingredient_name = models.CharField(max_length=100)
    numeric_amount = models.IntegerField(default=0)
    measurement_type = models.IntegerField(default=0)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class RecipeSteps(models.model):
    step = models.IntegerField(default=1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    direction = models.CharField(max_length=640)








