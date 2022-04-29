# Generated by Django 4.0.4 on 2022-04-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_sponsor_student_sponsor_sponsor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='is_legal_person',
        ),
        migrations.AlterField(
            model_name='student',
            name='allocated_money',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
