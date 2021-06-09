# Generated by Django 3.2.4 on 2021-06-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiqueitems',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='autobidsettings',
            name='owner',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid_owner',
            field=models.IntegerField(),
        ),
    ]