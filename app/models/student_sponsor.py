from django.db import models
from django.core.validators import MinValueValidator


class Student_sponsor(models.Model):
    spent_money = models.IntegerField()
    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} supplied by {self.sponsor}'


