from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
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
    list_filter = ("country", "city", "price", "rooms", "toilets", "pet_friendly" , "kind", "amenities","created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    # search_fields = ("^city", "^country",)
    
    
@admin.register(Amenity)    
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description","created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    # search_fields = ("^name",)
