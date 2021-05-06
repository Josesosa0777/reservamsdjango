from django.shortcuts import render, redirect
from django.http import HttpResponse
from people_app.models import PeopleList
from people_app.forms import PeopleForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from static.data.people_dictionary import people as show_people
from static.data.operation_data import question_operation
from static.data.strategist_data import question_strategist
from static.data.management_data import question_management
from static.data.operation_data_engineer import question_operation_engineer
from static.data.strategist_data_engineer import question_strategist_engineer
from static.data.management_data_engineer import question_management_engineer


@login_required
def people(request):
    # {} if I need to send any content
    if request.method == "POST":
        form = PeopleForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Person Added!"))
        return redirect('peoplelist')
    else:
        all_people = PeopleList.objects.all()
        paginator = Paginator(all_people, 5)  # number of items per page
        page = request.GET.get('pg')
        all_people = paginator.get_page(page)
        return render(request, 'peoplelist.html', {'all_people': all_people})


def contact(request):
    context = {
        'contact_text': 'Welcome to Contact page',
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': 'Welcome to About page',
    }
    return render(request, 'about.html', context)


@login_required
def delete_people(request, people_id):
    people = PeopleList.objects.get(pk=people_id)  # pk is for primary key
    people.delete()
    return redirect('peoplelist')


@login_required
def edit_people(request, people_id):
    if request.method == "POST":
        people = PeopleList.objects.get(pk=people_id)
        form = PeopleForm(request.POST or None, instance=people)
        if form.is_valid():
            form.save()
        messages.success(request, ("Person Edited!"))
        return redirect('peoplelist')
    else:
        people_obj = PeopleList.objects.get(pk=people_id)
        return render(request, 'edit.html', {'people_obj': people_obj})


def index(request):
    context = {
        'index_text': 'Welcome Index Page',
    }
    return render(request, 'index.html', context)
