from django.db import models
from fleet.models import Aircraft
from airport.models import Link, Node

# Create your models here.
class Runway(models.Model):
    runway_designator = models.CharField(max_length=3)
    length = models.FloatField()
    def __str__(self):
        return "RWY {}".format(self.runway_designator)
    
class Exit(models.Model):
    runway = models.ForeignKey(Runway, on_delete=models.CASCADE)
    taxiway = models.CharField(max_length=2)
    distance = models.FloatField()
    angle = models.FloatField()
    def __str__(self):
        return "TWY {}; {}".format(self.taxiway, self.runway)

class Results(models.Model):
    fleet = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    runway = models.ForeignKey(Link, on_delete=models.CASCADE)
    threshold = models.ForeignKey(Node, on_delete=models.CASCADE)
    def __str__(self):
        return self.name