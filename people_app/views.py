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
from datetime import datetime, timezone
import pytz
from evaluation_app.models import AnswerList
# from django.views.decorators.csrf import csrf_exempt


@login_required
def people(request):
    # {} if I need to send any content
    if request.method == "POST":
        print("POST formulario: ")
        print(request.POST)
        print("Esto ES")
        form = PeopleForm(request.POST or None)
        print(form)
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


@login_required
def contact(request):
    if request.method == "POST":
        form = request.POST

        # q1 = request.POST['C1']
        # a1 = request.POST['a1']
        # # return redirect(url_for("questions_by_area"))
        # print("NAME EVALUATED ")
        # print(name_evaluated + ", " + str(q1) + ", " + str(a1))
        # Get current user:
        current_user = str(request.user)
        values = []
        categories = []
        person_Leader = ""
        evaluator_name = ""
        questions = ""
        person_evaluated = str(form['name_person'])
        print(person_evaluated)
        all_people = PeopleList.objects.all()
        for name in all_people:
            if name.name == person_evaluated:
                person_Category = name.category
                person_Email = name.email
                person_Area = name.area
                person_Leader = name.leader
            if (current_user == name.email):
                evaluator_name = name.name
        if person_Area != "engineer":
            area_person = "not_engineer"
            if person_Category == "Operation":
                questions = question_operation
            elif person_Category == "Strategist":
                questions = question_strategist
            elif person_Category == "Direction":
                questions = question_management
        if person_Area == "engineer":
            area_person = "engineer"
            if person_Category == "Operation":
                questions = question_operation_engineer
            elif person_Category == "Strategist":
                questions = question_strategist_engineer
            elif person_Category == "Direction":
                questions = question_management_engineer
        # print(questions)
        # considera un else break...
        for q_ in range(0, len(questions)):
            if q_ % 3 == 0:
                # Compromiso Org., Pensamiento Anal.
                quest = questions[q_]["category"]
                categories.append(quest)
        if area_person == "not_engineer":
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
            c5 = 0
            c6 = 0
            c7 = 0
            c8 = 0
            # answer of the questions ans can be (0 -> 4)  añadi al final persona evaluada cómo afecta?
            print(person_Leader+" lead")
            if evaluator_name == person_Leader:
                for index in range(1, len(form)-5):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))  # Resultados de respuestas
                # example of working with matrix using numpy:
                # print(np.array(values)*2)
                q1 = form['Q1']
                q2 = form['Q2']
                q3 = form['Q3']
                q4 = form['Q4']
                if form['Q1'] == "":
                    q1 = 0
                if form['Q2'] == "":
                    q2 = 0
                if form['Q3'] == "":
                    q3 = 0
                if form['Q4'] == "":
                    q4 = 0
            if evaluator_name != person_Leader:
                for index in range(1, len(form)-1):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))
                    print(values)
                q1 = 0
                q2 = 0
                q3 = 0
                q4 = 0
        if area_person == "engineer":
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            if evaluator_name == person_Leader:
                for index in range(1, len(form)-9):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))
                    #
                c1 = form['C1']
                c2 = form['C2']
                c3 = form['C3']
                c4 = form['C4']
                c5 = form['C5']
                c6 = form['C6']
                c7 = form['C7']
                c8 = form['C8']
                if form['C1'] == "":
                    c1 = 0
                if form['C2'] == "":
                    c2 = 0
                if form['C3'] == "":
                    c3 = 0
                if form['C4'] == "":
                    c4 = 0
                if form['C5'] == "":
                    c5 = 0
                if form['C6'] == "":
                    c6 = 0
                if form['C7'] == "":
                    c7 = 0
                if form['C8'] == "":
                    c8 = 0
            if evaluator_name != person_Leader:
                for index in range(1, len(form)-1):
                    ind = "a" + str(index)
                    values.append(int(form[ind]))
                c1 = 0
                c2 = 0
                c3 = 0
                c4 = 0
                c5 = 0
                c6 = 0
                c7 = 0
                c8 = 0
        print(values)
        tz = pytz.timezone('America/Monterrey')
        monterrey_now = datetime.now(tz)
        print(monterrey_now)
        print(tz)
        new_answers = AnswerList.objects.create(
            evaluator=evaluator_name,
            evaluated_person=person_evaluated,
            email_evaluator=current_user,
            answers=str(values),
            Q1=q1, Q2=q2, Q3=q3, Q4=q4,
            C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7, C8=c8,
            category_answer=str(categories),
            answer_date=monterrey_now,
            leader=person_Leader
        )

    # Get current user:
    current_user = str(request.user)
    print(current_user)
    # Create dictionary with person Data from PeopleList
    list_people = []
    name_evaluator = ''
    all_people = PeopleList.objects.all()
    for name in all_people:
        personName = name.name
        personCategory = name.category
        personEmail = name.email
        personArea = name.area
        personLeader = name.leader
        personData = {
            'name': personName,
            'category': personCategory,
            'email': personEmail,
            'area': personArea,
            'leader': personLeader,
        }
        list_people.append(personData)

        if (current_user == personEmail):
            name_evaluator = personName
    # name_evaluated = form['name_person']

    # if show_people[name]['name'] == name_evaluated:
    #     category = show_people[name]['category']
    #     area = show_people[name]['area']
    #     leader_person = show_people[name]['leader']
    # if show_people[name]['email'] == current_user.email:
    #     name_evaluator = show_people[name]['name']
    return render(request, 'contact.html', {'list_people': list_people, 'name_evaluator': name_evaluator})
    # return render(request, "contact.html", email=current_user.email, name=current_user.name,
    #               questions_operation=question_operation, questions_strategist=question_strategist,
    #               questions_management=question_management, questions_operation_engineer=question_operation_engineer,
    #               questions_strategist_engineer=question_strategist_engineer, questions_management_engineer=question_management_engineer, people=people, logged_in=True,
    #               name_evaluated=name_evaluated, category=category, area=area, leader_person=leader_person,
    #               name_evaluator=name_evaluator, user=current_user.email)


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


# @csrf_exempt
def evaluation(request):
    if request.method == "POST":
        name_evaluated = request.POST['name_person']
        # ------------------
        # Get current user:
        current_user = str(request.user)
        print(current_user)
        # Create dictionary with person Data from PeopleList
        list_people = []
        name_evaluator = ''
        all_people = PeopleList.objects.all()
        for name in all_people:
            if name.name == name_evaluated:
                personCategory = name.category
                personEmail = name.email
                personArea = name.area
                personLeader = name.leader
            if (current_user == name.email):
                name_evaluator = name.name
                print(name_evaluator)
        data = {'email_evaluator': current_user, 'questions_operation': question_operation, 'questions_strategist': question_strategist,
                'questions_management': question_management, 'questions_operation_engineer': question_operation_engineer,
                'questions_strategist_engineer': question_strategist_engineer, 'questions_management_engineer': question_management_engineer,
                'logged_in': True, 'name_evaluated': name_evaluated, 'category': personCategory, 'area': personArea, 'leader_person': personLeader,
                'email': personEmail, 'name_evaluator': name_evaluator}
    return render(request, 'evaluation.html', data)


def submitted(request):
    if request.method == "POST":
        # with open("templates/strategist.html") as file:
        #    contents = file.read()
        #soup = BeautifulSoup(contents, "html.parser")
        # print(soup.prettify())
        values = []
        categories = []
        form = request.form
        leader_person = ""
        ind_ = []
        questions = ""
        person_evaluated = str(form['name_person'])
        print(person_evaluated)
        for index in people:
            if people[index]['name'] == person_evaluated:
                ind_ = index  # indice de persona evaluada
                leader_person = people[index]['leader']
            if people[index]['email'] == current_user.email:
                evaluator_name = people[index]['name']
        if ind_:
            print(ind_)
            if people[ind_]['area'] != "engineer":
                area_person = "not_engineer"
                if people[ind_]['category'] == "Operation":
                    questions = question_operation
                elif people[ind_]['category'] == "Strategist":
                    questions = question_strategist
                elif people[ind_]['category'] == "Direction":
                    questions = question_management
            if people[ind_]['area'] == "engineer":
                area_person = "engineer"
                if people[ind_]['category'] == "Operation":
                    questions = question_operation_engineer
                elif people[ind_]['category'] == "Strategist":
                    questions = question_strategist_engineer
                elif people[ind_]['category'] == "Direction":
                    questions = question_management_engineer
            # print(questions)
            # considera un else break...
            for q_ in range(0, len(questions)):
                if q_ % 3 == 0:
                    # Compromiso Org., Pensamiento Anal.
                    quest = questions[q_]["category"]
                    categories.append(quest)
        if area_person == "not_engineer":
            c1 = None
            c2 = None
            c3 = None
            c4 = None
            c5 = None
            c6 = None
            c7 = None
            c8 = None
            # answer of the questions ans can be (0 -> 4)  añadi al final persona evaluada cómo afecta?
            print(leader_person+" lead")
            if evaluator_name == leader_person:
                for index in range(1, len(form)-4):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))
                # example of working with matrix using numpy:
                # print(np.array(values)*2)
                q1 = form['Q1']
                q2 = form['Q2']
                q3 = form['Q3']
                q4 = form['Q4']
                if form['Q1'] == "":
                    q1 = None
                if form['Q2'] == "":
                    q2 = None
                if form['Q3'] == "":
                    q3 = None
                if form['Q4'] == "":
                    q4 = None
            if evaluator_name != leader_person:
                for index in range(1, len(form)):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))
                q1 = None
                q2 = None
                q3 = None
                q4 = None
        if area_person == "engineer":
            q1 = None
            q2 = None
            q3 = None
            q4 = None
            if evaluator_name == leader_person:
                for index in range(1, len(form)-8):
                    ind = "a"+str(index)
                    values.append(int(form[ind]))
                    #
                c1 = form['C1']
                c2 = form['C2']
                c3 = form['C3']
                c4 = form['C4']
                c5 = form['C5']
                c6 = form['C6']
                c7 = form['C7']
                c8 = form['C8']
                if form['C1'] == "":
                    c1 = None
                if form['C2'] == "":
                    c2 = None
                if form['C3'] == "":
                    c3 = None
                if form['C4'] == "":
                    c4 = None
                if form['C5'] == "":
                    c5 = None
                if form['C6'] == "":
                    c6 = None
                if form['C7'] == "":
                    c7 = None
                if form['C8'] == "":
                    c8 = None
            if evaluator_name != leader_person:
                for index in range(1, len(form)):
                    ind = "a" + str(index)
                    values.append(int(form[ind]))
                c1 = None
                c2 = None
                c3 = None
                c4 = None
                c5 = None
                c6 = None
                c7 = None
                c8 = None
        tz = pytz.timezone('America/Monterrey')
        monterrey_now = datetime.now(tz)
        new_answers = Team(
            evaluator=evaluator_name,
            evaluated_person=person_evaluated,
            email_evaluator=current_user.email,
            answers=str(values),
            Q1=q1,
            Q2=q2,
            Q3=q3,
            Q4=q4,
            C1=c1,
            C2=c2,
            C3=c3,
            C4=c4,
            C5=c5,
            C6=c6,
            C7=c7,
            C8=c8,
            category_answer=str(categories),
            answer_date=monterrey_now,
            leader=leader_person
        )
        db.session.add(new_answers)
        db.session.commit()
        # get_answer_database()
    return redirect(url_for('questions_by_area'))
