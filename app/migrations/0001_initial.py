# Generated by Django 4.0.4 on 2022-04-21 06:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('payment_amount', models.IntegerField()),
                ('spent_money', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('is_legal_person', models.BooleanField()),
                ('organization_name', models.CharField(blank=True, editable=False, max_length=200)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('Moderatsiyada', 'Moderatsiyada'), ('Bekor_qilingan', 'Bekor qilingan'), ('Tasdiqlangan', 'Tasdiqlangan')], default='Yangi', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('degree', models.CharField(choices=[('BAKALAVR', 'Bakalavr'), ('MAGISTR', 'Magistr')], max_length=20)),
                ('contract_sum', models.FloatField()),
                ('allocated_money', models.IntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student_sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spent_money', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('Sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sponsor')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.university'),
        ),
    ]
