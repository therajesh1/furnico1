# Generated by Django 3.1.12 on 2025-02-06 13:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipapplications',
            name='resume',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='resume'),
        ),
    ]
