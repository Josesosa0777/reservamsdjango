from django.shortcuts import render, redirect
from django.http import HttpResponse
from people_app.models import PeopleList
from people_app.forms import PeopleForm
from django.contrib import messages


def people(request):
    # {} if I need to send any content
    if request.method == "POST":
        form = PeopleForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Person Added!"))
        return redirect('peoplelist')
    else:
        all_people = PeopleList.objects.all
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


def delete_people(request, people_id):
    people = PeopleList.objects.get(pk=people_id)  # pk is for primary key
    people.delete()
    return redirect('peoplelist')


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
