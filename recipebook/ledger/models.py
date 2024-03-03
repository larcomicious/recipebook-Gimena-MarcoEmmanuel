from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    

class RecipeIngredient(models.Model):
    quantity = models.FloatField(max_length=100)
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete = models.CASCADE,
        related_name = 'ingredients'
    )
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )
