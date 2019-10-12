# Generated by Django 2.2.5 on 2019-10-12 12:39

import boards.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to=boards.models.article_image_path),
            preserve_default=False,
        ),
    ]
