# Generated by Django 4.0.2 on 2022-04-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50, null=True)),
                ('file', models.FileField(upload_to='input')),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
