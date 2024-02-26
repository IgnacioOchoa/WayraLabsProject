from django.contrib import admin
from .models import Node, Link

# Register your models here.

class NodeAdmin(admin.ModelAdmin):
    list_display=("__str__", "x", "y", "type")

class LinkAdmin(admin.ModelAdmin):
    list_display=("__str__", "description")

admin.site.register(Node, NodeAdmin)
admin.site.register(Link, LinkAdmin)
