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
import numpy as np
# from django.views.decorators.csrf import csrf_exempt


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


@login_required
def start_evaluation(request):
    if request.method == "POST":
        comment_1 = ''
        comment_2 = ''
        form = request.POST
        print(form)
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
                comment_1 = form['comment_1']
                comment_2 = form['comment_2']
                for index in range(1, len(form)-7):
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
                comment_1 = form['comment_1']
                comment_2 = form['comment_2']
                for index in range(1, len(form)-11):
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
            leader=person_Leader,
            comment_1=comment_1, comment_2=comment_2
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
    return render(request, 'start_evaluation.html', {'list_people': list_people, 'name_evaluator': name_evaluator})


@login_required
def evaluated_people(request):
    current_user = str(request.user)
    all_answer = AnswerList.objects.all()
    if request.method == "POST":
        form = request.POST
        chosen_person = form['person_id']
        stored_answers = []  # answers of team evaluation
        self_stored_answers = []  # answers of autoevaluation
        mean_okr = ''
        team_evaluation = []
        result_okr = []
        x_ans = []
        comment_1 = ''
        comment_2 = ''
        # evalua cuando los resultados de cuando la persona aparece en la db
        for person in all_answer:
            if chosen_person == person.evaluated_person and person.evaluator == chosen_person:
                self_ans = person.answers
                self_ans = self_ans.replace(' ', '')
                self_ans = self_ans.replace("'", "")
                self_ans = self_ans.replace("[", "")
                self_ans = self_ans.replace("]", "")
                # convert the string to an array
                self_ans = self_ans.split(",")
                # array of number for answer:
                # convert to an array of numbers
                self_ans_array = [int(numeric) for numeric in self_ans]
                # conversion of answer to percentage:
                self_ans_conversion = []
                for n in range(0, len(self_ans_array)):
                    self_ans_ = self_ans_array[n]
                    if self_ans_ == 1:
                        self_ans_ = 25
                    elif self_ans_ == 2:
                        self_ans_ = 50
                    elif self_ans_ == 3:
                        self_ans_ = 75
                    elif self_ans_ == 4:
                        self_ans_ = 100
                    self_ans_conversion.append(self_ans_)
                self_stored_answers.append(self_ans_conversion)
                category = person.category_answer.split(",")
                category = [s.replace("[", "") for s in category]
                category = [s.replace("]", "") for s in category]
                category = [s.replace("'", "") for s in category]
            if chosen_person == person.evaluated_person and person.evaluator != chosen_person:
                val_okrs = []
                val_okrs.append(person.Q1)
                val_okrs.append(person.Q2)
                val_okrs.append(person.Q3)
                val_okrs.append(person.Q4)
                val_okrs.append(person.C1)
                val_okrs.append(person.C2)
                val_okrs.append(person.C3)
                val_okrs.append(person.C4)
                val_okrs.append(person.C5)
                val_okrs.append(person.C6)
                val_okrs.append(person.C7)
                val_okrs.append(person.C8)
                comment_1 = person.comment_1
                comment_2 = person.comment_2
                result_mean_okrs = np.average(
                    [x for x in val_okrs if x != 0])
                if result_mean_okrs > 0:
                    mean_okr = result_mean_okrs
                ans = person.answers
                ans = ans.replace(' ', '')
                ans = ans.replace("'", "")
                ans = ans.replace("[", "")
                ans = ans.replace("]", "")
                ans = ans.split(",")  # convert the string to an array
                # array of number for answer:
                # convert to an array of numbers
                ans_array = [int(numeric_string) for numeric_string in ans]
                # conversion of answer to percentage:
                ans_conversion = []
                for n_ans in range(0, len(ans_array)):
                    ans_ = ans_array[n_ans]
                    if ans_ == 1:
                        ans_ = 25
                    elif ans_ == 2:
                        ans_ = 50
                    elif ans_ == 3:
                        ans_ = 75
                    elif ans_ == 4:
                        ans_ = 100
                    ans_conversion.append(ans_)
                stored_answers.append(ans_conversion)

                category = person.category_answer.split(",")
                category = [s.replace("[", "") for s in category]
                category = [s.replace("]", "") for s in category]
                category = [s.replace("'", "") for s in category]
                print(category)
        # average of array: https://stackoverflow.com/questions/2153444/python-finding-average-of-a-nested-list/2157646
        if stored_answers:
            answers_mean = np.mean(stored_answers, axis=0)
            # cada 3 respuestas me debe dar una gráfica, entonces hay que promediar cada 3 respuestas:
            x_ans = []
            for i in range(0, len(answers_mean)):
                if (i+1) % 3 == 0:
                    elem_mean = np.mean(answers_mean[i-2:i+1])
                    # almacena promed. cada 3 elements (el num de preguntas deben ser múltiplo de 3)
                    x_ans.append(elem_mean)
            x_ans = np.round(x_ans, decimals=2)
            # Evaluación del team Competencias
            team_evaluation = np.round(np.mean(x_ans*0.3), decimals=2)

        if self_stored_answers:
            self_answers_mean = np.mean(self_stored_answers, axis=0)
            self_x_ans = []
            for i in range(0, len(self_answers_mean)):
                if (i+1) % 3 == 0:
                    self_elem_mean = np.mean(self_answers_mean[i-2:i+1])
                    # almacena promed. cada 3 elements (el num de preguntas deben ser múltiplo de 3)
                    self_x_ans.append(self_elem_mean)
            self_x_ans = np.round(self_x_ans, decimals=2)
            # Resultados
            self_evaluation = np.round(
                np.mean(self_answers_mean*0.3), decimals=2)

        # remove the space before and after each element of the category
        number_elements = []
        for elem in range(0, len(category)):
            number_elements.append(elem)
            category[elem] = category[elem].strip()

        y_ans = category

        if mean_okr and team_evaluation:
            result_okr = np.round(mean_okr*0.7, decimals=2)
            total_evaluation = np.round(
                (team_evaluation + result_okr), decimals=2)
        elif not mean_okr and team_evaluation:
            result_okr = '-- '
            total_evaluation = team_evaluation
        else:
            total_evaluation = '--'
        # ---------

        print("RESULT OKR ")
        print(result_okr)
        print(team_evaluation)
        return render(request, 'results.html', {'person': chosen_person, 'options': all_answer, 'self_x_values': self_x_ans,
                                                'x_values': x_ans, 'y_values': y_ans, 'team_evaluation': team_evaluation,
                                                'result_okr': result_okr, 'self_evaluation': self_evaluation, 'total_evaluation': total_evaluation,
                                                'actual_user': current_user, 'comment_1': comment_1, 'comment_2': comment_2, 'number_elements': number_elements})
    # current_user = str(request.user)
    # all_answer = AnswerList.objects.all()
    names = []
    for name in all_answer:
        names.append(name.evaluated_person)
    my_name_list = list(set(names))  # get list with no duplicated names
    print(my_name_list)
    paginator = Paginator(my_name_list, 10)  # number of items per page
    page = request.GET.get('pg')
    my_name_list = paginator.get_page(page)
    return render(request, 'evaluated_people.html', {'actual_user': current_user, 'options': my_name_list})


@login_required
def all_results(request):
    all_answer = AnswerList.objects.all()
    print(all_answer)
    paginator = Paginator(all_answer, 10)  # number of items per page
    page = request.GET.get('pg')
    all_answer = paginator.get_page(page)
    return render(request, 'all_results.html', {'all_answer': all_answer})


@login_required
def delete_people(request, people_id):
    people = PeopleList.objects.get(pk=people_id)  # pk is for primary key
    current_user = str(request.user)
    if current_user == 'edith@reservamos.mx':
        people.delete()
    else:
        messages.error(request, ("Access Restricted, You Are Not Allowed."))
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
@login_required
def evaluation(request):
    if request.method == "POST":
        name_evaluated = request.POST['name_person']
        # ------------------
        # Get current user:
        current_user = str(request.user)
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
        data = {'email_evaluator': current_user, 'questions_operation': question_operation, 'questions_strategist': question_strategist,
                'questions_management': question_management, 'questions_operation_engineer': question_operation_engineer,
                'questions_strategist_engineer': question_strategist_engineer, 'questions_management_engineer': question_management_engineer,
                'logged_in': True, 'name_evaluated': name_evaluated, 'category': personCategory, 'area': personArea, 'leader_person': personLeader,
                'email': personEmail, 'name_evaluator': name_evaluator}
        print("THE DATA")
    return render(request, 'evaluation.html', data)
