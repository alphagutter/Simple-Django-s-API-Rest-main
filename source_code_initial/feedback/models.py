from django.db import models

# this model is for a simple table for 'Products'

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name