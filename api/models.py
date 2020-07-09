from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length = 50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length = 15)

    def __str__(self):
        return self.name

    def welcomer(self):
        return "Welcome back, {}!".format(self.name)

class Aircraft(models.Model):
    registration = models.CharField(max_length = 10)
    serial_number = models.IntegerField(default = 0)
    aircraft_class = models.CharField(max_length = 20)
    aircraft_type = models.CharField(max_length = 50)
    number_of_seats = models.IntegerField(default = 1)
    cost_per_hour = models.IntegerField(default = 0)
    home_base = models.CharField(max_length = 50)
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)

    def __str__(self):
        return self.registration