# Generated by Django 2.2.5 on 2019-10-09 18:54

import board.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to=board.models.articles_image_path),
            preserve_default=False,
        ),
    ]