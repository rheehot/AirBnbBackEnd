from django.db import models


class House(models.Model):

    """ HOUSE MODEL DEFINITION """

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price per night", help_text="Positive number only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed",
        default=True,
        help_text="Does this house allow pets?",
    )
    
    owner = models.ForeignKey("users.User",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
