from django.db import models
from django.core.validators import MinValueValidator
from rest_framework import serializers


New = 'Yangi'
Moderation = 'Moderatsiyada'
Denied = 'Bekor_qilingan'
Approved = 'Tasdiqlangan'

Choices = (
    (New, 'Yangi'),
    (Moderation, 'Moderatsiyada'),
    (Denied, 'Bekor qilingan'),
    (Approved, "Tasdiqlangan"),
)


class Sponsor(models.Model):
    full_name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    payment_amount = models.IntegerField()
    spent_money = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    organization_name = models.CharField(max_length=200, blank=True, editable=False)
    status = models.CharField(max_length=200, choices=Choices, default=New)

    def __str__(self):
        return self.full_name
