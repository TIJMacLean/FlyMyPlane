from django.contrib import admin

# Register your models here.
from .models import Question, Choices, FlightCategories

admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(FlightCategories)