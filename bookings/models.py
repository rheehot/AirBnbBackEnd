from django.db import models
from common.models import CommonModel

class Booking(CommonModel):
        
        """ Booking Model Definition """
        class BookingKindChoices(models.TextChoices):
            ROOM = "room", "Room"
            EXPERIENCE = "experience", "Experience"
        
        
        kind = models.CharField(max_length=20,choices=BookingKindChoices.choices)
        user = models.ForeignKey("users.User", on_delete=models.CASCADE)
        room = models.ForeignKey("rooms.Room",
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
        experience = models.ForeignKey("experiences.Experience",
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL)
        check_in = models.DateField()
        check_out = models.DateField()
        experience_time = models.DateTimeField()
        guests = models.PositiveIntegerField()
        
        def __str__(self) -> str:
            return f"{self.kind.title()} booking for {self.user}"