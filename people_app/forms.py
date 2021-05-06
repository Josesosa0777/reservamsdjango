from django import forms
from people_app.models import PeopleList


class PeopleForm(forms.ModelForm):
    class Meta:
        model = PeopleList
        fields = ['name', 'category', 'email', 'area', 'leader']
