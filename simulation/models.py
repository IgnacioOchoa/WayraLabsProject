from django.db import models
from fleet.models import Aircraft
from airport.models import Link, Node

# Create your models here.
class Results(models.Model):
    fleet = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    runway = models.ForeignKey(Link, on_delete=models.CASCADE)
    threshold = models.ForeignKey(Node, on_delete=models.CASCADE)
    def __str__(self):
        return self.name