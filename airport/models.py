from django.db import models
# Create your models here.

class Node(models.Model):
    x = models.FloatField()
    y = models.FloatField()

class Link(models.Model):
    node1 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node1')
    node2 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node2')
    description = models.TextField()
