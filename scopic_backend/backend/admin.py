from django.contrib import admin

# Register your models here.
from backend.models import AntiqueItems, Bids

admin.site.register(AntiqueItems)
admin.site.register(Bids)