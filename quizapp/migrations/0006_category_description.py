# Generated by Django 4.2.3 on 2023-07-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_useranswer_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='done'),
            preserve_default=False,
        ),
    ]
