# Generated by Django 3.0 on 2022-05-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
