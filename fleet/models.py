from django.db import models

class Aircraft(models.Model):
    name = models.CharField(max_length = 25)
    icao_id = models.CharField(max_length = 5)
    landing_speed = models.IntegerField()
    landing_distance = models.IntegerField()
    mtow = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
class Fleet(models.Model):
    name = models.CharField(max_length = 25)
    aircrafts = models.ManyToManyField(Aircraft, through='AircraftQuantity')

    def __str__(self):
        return self.name

class AircraftQuantity(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.fleet.__str__(), self.aircraft.__str__())