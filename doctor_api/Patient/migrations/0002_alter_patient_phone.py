# Generated by Django 4.0.6 on 2022-07-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]