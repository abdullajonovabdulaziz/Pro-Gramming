# Generated by Django 5.0.1 on 2024-03-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_alter_video_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
