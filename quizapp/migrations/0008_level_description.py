# Generated by Django 4.2.3 on 2023-07-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0007_category_image_level_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='description',
            field=models.TextField(default='done description'),
            preserve_default=False,
        ),
    ]
