# Generated by Django 4.2.6 on 2023-11-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_exteriorcamion_capot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
