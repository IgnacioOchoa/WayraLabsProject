from django.db import models
# Create your models here.

class Node(models.Model):
    class Type(models.TextChoices):
        INT = "1", "INTERSECTION"
        THR = "2", "THRESHOLD/END"
        DTH = "3", "DISPLACED THRESHOLD"
        STP = "4", "STOPBAR"
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.INT
    )
    runway_designator= models.CharField(
        max_length=3,
    )

    def __str__(self):
        return "{} {}".format(self.get_type_display(),self.runway_designator)

class Link(models.Model):
    class Type(models.TextChoices):
        RWY = "1", "RUNWAY"
        TWY = "2", "TAXIWAY"
        APR = "3", "APRON"
    node1 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node1')
    node2 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node2')
    width = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.TWY
    )

    def __str__(self):
        return "{}, {} to {}".format(self.get_type_display(),self.node1,self.node2)
