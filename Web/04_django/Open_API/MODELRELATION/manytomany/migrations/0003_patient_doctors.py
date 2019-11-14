# Generated by Django 2.2.5 on 2019-11-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0002_auto_20191113_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(through='manytomany.Reservation', to='manytomany.Doctor'),
        ),
    ]
