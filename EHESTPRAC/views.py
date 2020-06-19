from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader
from django.http import HttpResponse

from .models import Question, Choices, FlightCategories
from .scorer import score

# Create your views here.

def index(request):
    template = loader.get_template('EHESTPRAC/index.html')
    context = {
        "pages": FlightCategories.objects.all()
    }
    return HttpResponse(template.render(context, request))


def checklist(request, flight_category):
    template = loader.get_template('EHESTPRAC/checklist.html')
    quest = Question.objects.filter(flight_category__flight_categories = flight_category)
    # choices = Choices.objects.all()
    category_name = FlightCategories.objects.get(flight_categories = flight_category)
    context = {
        "flight_category_name": category_name,
        "questions": quest,
        # "choices": choices
    }
    return HttpResponse(template.render(context, request))


def results(request, flight_category):
    template = loader.get_template('EHESTPRAC/results.html')
    choices = {}
    for request_key in request.POST:
        if request_key[:7] == "choices":
            question_id = request_key[7:]
            choices[question_id] = request.POST[request_key]
    num_questions = len(choices)
    risk, flight_score, risk_numeric, risk_numeric_as_percentage = score(choices, num_questions)
    context = {
        "score": flight_score,
        "num_qs": num_questions,
        "risk": risk,
        "risk_numeric": risk_numeric,
        "risk_numeric_as_percentage": risk_numeric_as_percentage
    }
    return HttpResponse(template.render(context, request))