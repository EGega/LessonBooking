# Generated by Django 4.1.5 on 2023-01-22 22:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdata', '0010_alter_teachers_teacher_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='after_lesson_comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
