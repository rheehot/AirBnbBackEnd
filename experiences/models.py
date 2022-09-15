from django.db import models
from common.models import CommonModel

class Experience(CommonModel):
    
    """ Experience Model Definition """
    
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start_at = models.TimeField()
    end_at = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    def __str__(self) -> str:
        return self.name
    
    
class Perk(CommonModel):
    
    """ Perk Model Definition """
    
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=150, null=True, blank=True)
    explanation = models.TextField(max_length=150, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    