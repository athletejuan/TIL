# Generated by Django 2.2.5 on 2019-11-18 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_like_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pk']},
        ),
    ]