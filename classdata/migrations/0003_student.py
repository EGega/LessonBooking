# Generated by Django 4.1.5 on 2023-01-21 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdata', '0002_teachers_teacher_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('profile_photo', models.ImageField(blank=True, upload_to='studentImgs')),
            ],
        ),
    ]
