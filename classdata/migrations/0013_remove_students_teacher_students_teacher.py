# Generated by Django 4.1.5 on 2023-01-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdata', '0012_remove_students_teacher_students_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='teacher',
        ),
        migrations.AddField(
            model_name='students',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='classdata.teachers'),
        ),
    ]
