import uuid
from django.db import models

# Create your models here.
class Recipe(models.model):
    recipe_id = models.UUIDField(primary_key=True, default=uuid.uuid64, editable=False)
    recipe_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)


class MeasurementTypes(models.model):
    recipe_id = models.UUIDField(primary_key=True, default=uuid.uuid64, editable=False)
    char_field = models.CharField(max_length=100)


class Ingedient(models.model):
    ingredient_name = models.CharField(max_length=100)
    numeric_amount = models.IntegerField(default=0)
    measurement_type = models.ForeignKey(MeasurementTypes, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class MeasurementConversion(models.model):
    




