from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError


class Student_sponsor(models.Model):
    spent_money = models.IntegerField()
    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} supplied by {self.sponsor}'


@receiver(pre_save, sender=Student_sponsor)
def check_payment(sender, instance, **kwargs):
    if instance.spent_money+instance.sponsor.spent_money>instance.sponsor.payment_amount:
        raise ValidationError(f"You can not pay more than {instance.sponsor.payment_amount-instance.sponsor.spent_money}")
    if instance.spent_money+instance.student.allocated_money>instance.student.contract_sum:
        raise ValidationError(f'You can not pay more than {instance.contract_sum-instance.student.allocated_money}')
