from django.db import models
from django.db.models import CASCADE


class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    item = models.ForeignKey("Item", related_name="chars", on_delete=CASCADE)


class Photo(models.Model):
    link = models.URLField(max_length=255)
    item = models.ForeignKey("Item", related_name="photos", on_delete=CASCADE)


class Item(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    memory = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    action_price = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    reviews_count = models.IntegerField(blank=True, null=True)
    screen_size = models.CharField(max_length=255, blank=True, null=True)
    screen_power = models.CharField(max_length=255, blank=True, null=True)
