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
    quest = Question.objects.filter(flight_category__flight_categories = flight_category).order_by("question_text")
    choices = Choices.objects.all().order_by("score")
    category_name = FlightCategories.objects.get(flight_categories = flight_category)
    
    context = {
        "flight_category_name": category_name,
        "questions": quest,
        "choices": choices
    }
    return HttpResponse(template.render(context, request))


def results(request, flight_category):
    template = loader.get_template('EHESTPRAC/results.html')
    data = {}

    for request_key in request.POST:
        if request_key[:7] == "choices":
            question_id = request_key[7:]
            data[Question.objects.get(id = question_id).question_text].update({
                "Choice": Choices.objects.filter(question__id = question_id).get(score = request.POST[request_key]),
                "ChoiceScore": request.POST[request_key]
            })
        elif request_key[:10] == "mitigation":
            question_id = request_key[10:]
            data[Question.objects.get(id = question_id).question_text].update({
                "MitigationScore": request.POST[request_key]
            })
        elif request_key[:8] == "mit_text":
            question_id = request_key[8:]
            data[Question.objects.get(id = question_id).question_text] = {
                "MitigationText": request.POST[request_key]
            }

    num_questions = len(data)
    risk, flight_score, mitigated_score, risk_numeric, risk_numeric_as_percentage, risk_numeric_mitigated, risk_numeric_as_percentage_mitigated, data = score(num_questions, data)

    context = {
        "flight_score": flight_score,
        "mitigated_score": mitigated_score,
        "num_qs": num_questions,
        "risk": risk,
        "risk_numeric": risk_numeric,
        "risk_numeric_as_percentage": risk_numeric_as_percentage,
        "risk_numeric_mitigated": risk_numeric_mitigated,
        "risk_numeric_as_percentage_mitigated": risk_numeric_as_percentage_mitigated,
        "data": data
    }
    return HttpResponse(template.render(context, request))
