from django.db import models
from django.utils import timezone


# Create your models here.
class TribeName(models.Model):
    gamename = models.TextField()
    game = models.ForeignKey("TribeGame", on_delete=models.CASCADE, null=False, blank=False)


class TribeGame(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-time']
