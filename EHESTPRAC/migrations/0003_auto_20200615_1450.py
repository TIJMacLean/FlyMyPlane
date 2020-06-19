# Generated by Django 3.0.7 on 2020-06-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EHESTPRAC', '0002_auto_20200615_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightcategories',
            name='flight_category',
        ),
        migrations.AddField(
            model_name='flightcategories',
            name='flight_categories',
            field=models.CharField(default='HEMSSP, HEMSMC, CATSP, CATMC, Training, Private, Maintenance, Firefighting', max_length=100),
            preserve_default=False,
        ),
    ]