from django.contrib import admin
from people_app.models import PeopleList
from evaluation_app.models import AnswerList

# Register your models here.
admin.site.register(PeopleList)
admin.site.register(AnswerList)
