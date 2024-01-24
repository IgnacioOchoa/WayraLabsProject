from django.db import models

# Create your models here.
class Fleet(models.Model):
    name = models.CharField(max_length = 5)
    app_speed = models.IntegerField()
    quantity = models.IntegerField()
