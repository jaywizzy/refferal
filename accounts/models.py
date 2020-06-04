from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referrer')
    referred = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred')

    class Meta:
        unique_together = (('referrer', 'referred'), )

    def __str__(self):
        return str(self.referrer)
