from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from .models import Referral


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile saved")

# post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        print("profile saved")

# post_save.connect(update_profile, sender=User)


# @receiver(post_save, sender=User)
# def create_referral(sender, instance, created, **kwargs):
#     if created:
#         Referral.objects.create(
#             referred=instance
#         )
#         print("referred created")
