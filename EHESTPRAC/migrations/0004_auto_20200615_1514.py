# Generated by Django 3.0.7 on 2020-06-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EHESTPRAC', '0003_auto_20200615_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightcategories',
            name='category',
        ),
        migrations.AddField(
            model_name='flightcategories',
            name='category',
            field=models.ManyToManyField(to='EHESTPRAC.Question'),
        ),
    ]
