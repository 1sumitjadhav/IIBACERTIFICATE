# Generated by Django 4.0.2 on 2022-04-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
