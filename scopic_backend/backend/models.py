from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AntiqueItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Bids(models.Model):
    antique_item = models.ForeignKey(AntiqueItems, on_delete=models.PROTECT)
    bid_price = models.FloatField()
    user = models.IntegerField()  # for dummy user id
    timestamp = models.DateTimeField(auto_now_add=True)


class AutoBid(models.Model):
    antique_item = models.ForeignKey(AntiqueItems, on_delete=models.PROTECT)
    user = models.IntegerField()  # for dummy user id
    is_automatic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AutoBidSettings(models.Model):
    user = models.IntegerField()  # for dummy user id
    balance = models.FloatField(default=0)
    bid_increase_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
