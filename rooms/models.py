from django.db import models

class Room(models.Model):
    country = models.CharField(max_length=140,)
