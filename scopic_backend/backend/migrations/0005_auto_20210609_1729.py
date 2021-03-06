# Generated by Django 3.2.4 on 2021-06-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210607_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autobidsettings',
            name='max_bid_amount',
        ),
        migrations.RemoveField(
            model_name='autobidsettings',
            name='my_money',
        ),
        migrations.AddField(
            model_name='autobidsettings',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='autobidsettings',
            name='bid_increase_amount',
            field=models.FloatField(default=0),
        ),
    ]
