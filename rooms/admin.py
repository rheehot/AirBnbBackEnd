from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "description",
        "address",
        "pet_friendly",
        "kind",
        "owner",
    )
    list_filter = ("country", "city", "price", "rooms", "toilets", "pet_friendly" , "kind", "amenities",)
    # search_fields = ("^city", "^country",)
    
    
@admin.register(Amenity)    
class AmenityAdmin(admin.ModelAdmin):
    pass
    # list_display = ("name", "description",)
    # search_fields = ("^name",)
