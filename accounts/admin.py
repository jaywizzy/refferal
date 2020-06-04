from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)


class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referrer', 'referred')


admin.site.register(Referral, ReferralAdmin)
