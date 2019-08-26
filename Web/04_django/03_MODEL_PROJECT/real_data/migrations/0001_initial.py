# Generated by Django 2.2.4 on 2019-08-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('rank', models.IntegerField()),
                ('keyword', models.CharField(max_length=30)),
            ],
        ),
    ]
