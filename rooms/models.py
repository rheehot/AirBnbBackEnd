from turtle import update
from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """ Room Model Definition """

    class RoomKindChoices(models.TextChoices):
        ENTIRE = ("entire", "Entire Place")
        PRIVATE = ("private", "Private Room")
        SHARED = ("shared", "Shared Room")

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20,
                            choices=RoomKindChoices.choices,)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms",)


class Amenity(CommonModel):

    """ Amenity Model Definition """

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=150, null=True, blank=True)
    # rooms = models.ManyToManyField(Room, related_name="amenities")
