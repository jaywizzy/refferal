from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_name

