# Generated by Django 3.0.7 on 2020-07-07 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=10)),
                ('serial_number', models.IntegerField(default=0)),
                ('aircraft_class', models.CharField(max_length=20)),
                ('aircraft_type', models.CharField(max_length=50)),
                ('number_of_seats', models.IntegerField(default=1)),
                ('cost_per_hour', models.IntegerField(default=0)),
                ('home_base', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Owner')),
            ],
        ),
    ]
