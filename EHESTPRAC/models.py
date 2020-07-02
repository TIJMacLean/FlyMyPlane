from django.db import models

# Create your models here.

class FlightCategories(models.Model):
    def __str__(self):
        return self.category_name

    flight_categories = models.CharField(max_length=100)
    category_name = models.CharField(max_length=30)

class Question(models.Model):
    def __str__(self):
        return self.question_text

    flight_category = models.ManyToManyField(FlightCategories)
    question_text = models.CharField(max_length=100)
    question_order = models.IntegerField(default=999)

class Choices(models.Model):
    def __str__(self):
        return self.choice_text

    def ordered_choices_set(self):
        return self.choices_set.all().order_by('self.score')

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    score = models.IntegerField(default=0)