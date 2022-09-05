from django.db import models

# Create your models here.
class Game(models.Model):
    room_code = models.CharField(max_length=100)
    host = models.CharField(max_length=200)
    join = models.CharField(max_length=200, default="",blank=True,null=True)
    game_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room_code