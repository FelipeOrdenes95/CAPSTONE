# Generated by Django 4.2.6 on 2023-11-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_camion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='estado',
            field=models.BooleanField(null=True),
        ),
    ]
