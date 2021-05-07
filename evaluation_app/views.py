from django.shortcuts import render, redirect
from django.http import HttpResponse
from evaluation_app.models import AnswerList
from datetime import datetime, timezone
import pytz
# from evaluation_app.forms import AnswerForm
# Create your views here.

tz = pytz.timezone('America/Monterrey')
monterrey_now = datetime.now(tz)


def evaluation(request):
    answer_instance = AnswerList.objects.create(
        evaluator='test',
        evaluated_person='Jhon',
        email_evaluator="",
        answers="",
        Q1=0, Q2=0, Q3=0, Q4=0,
        C1=0, C2=0, C3=0, C4=0, C5=0, C6=0, C7=0, C8=0,
        category_answer="",
        answer_date=monterrey_now,
        leader="")

    return render(request, 'evaluation_form.html', {})
