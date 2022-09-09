from unicodedata import name
from django.db import models

class Dish(models.Model):
  image = models.ImageField()
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=300)
  price = models.FloatField()

  def __str__(self):
    return self.name
