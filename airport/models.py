from django.db import models
# Create your models here.

class Node(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return "Node " + str(self.id)

class Link(models.Model):
    node1 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node1')
    node2 = models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name='link_node2')
    description = models.TextField()

    def __str__(self):
        return "Link {} (N{}-N{})".format(self.id,self.node1.id,self.node2.id)
