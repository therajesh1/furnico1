# Generated by Django 3.1.12 on 2025-02-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0005_auto_20250206_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipApplications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('college', models.TextField()),
                ('year', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('role', models.CharField(choices=[('Developer', 'Developer'), ('Designer', 'Designer'), ('Marketing', 'Marketing')], max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.DeleteModel(
            name='InternshipApplication',
        ),
    ]
