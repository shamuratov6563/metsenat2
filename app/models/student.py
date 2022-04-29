from django.db import models

Bachelor = 'BAKALAVR'
Master = 'MAGISTR'

choices = [
    (Bachelor, 'Bakalavr'),
    (Master, 'Magistr'),
]


class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20, choices=choices)
    contract_sum = models.FloatField()
    sponsor = models.ManyToManyField('Sponsor', through='Student_sponsor', through_fields=('student', 'sponsor'), blank=True)
    allocated_money = models.IntegerField(default=0,  editable=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name


