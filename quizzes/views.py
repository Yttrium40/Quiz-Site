from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from users.utils import get_current_user

from .models import Quiz, Question, Choice
from .utils import validate_nonempty_quiz_elements
import copy


def create(request):
    return render(request, 'quizzes/create.html', {
        'current_user': get_current_user(request)
    })

def creating(request):
    # get questions
    post_copy = copy.deepcopy(request.POST)
    question_list = []
    choice_dict = {}
    quiz_name = ''
    curr_question_index = 0
    do_loop = True
    while do_loop:
        do_loop = False
        for key in post_copy:
            val = post_copy[key]
            if val is None:
                continue

            contains_question = key.count('question') == 1
            contains_choice = key.count('choice') == 1

            # question_1_choice_1
            if contains_question and contains_choice:
                split = key.split('_')
                question_index = int(split[1])
                choice_index = int(split[-1])
                dict_val = choice_dict.get(question_index)
                if dict_val is None:
                    choice_dict[question_index] = [val]
                    post_copy[key] = None
                elif len(dict_val) is choice_index:
                    dict_val.append(val)
                    post_copy[key] = None
                do_loop = True

            # question_1
            elif contains_question:
                if key.endswith(str(curr_question_index)):
                    question_list.append(val)
                    curr_question_index += 1
                    post_copy[key] = None
                    do_loop = True
            elif key is not 'csrfmiddlewaretoken':
                quiz_name = val
                post_copy[key] = None

    error_messages = validate_nonempty_quiz_elements(quiz_name, question_list, choice_dict)
    if error_messages != []:
        return render(request, 'quizzes/create.html', {
            'current_user': get_current_user(request),
            'error_messages': error_messages
        })

    user = get_current_user(request)
    new_quiz = Quiz(author=user, name=quiz_name)
    new_quiz.save()

    index = 0
    for question in question_list:
        new_question = Question(quiz=new_quiz, text=question)
        new_question.save()
        for choice in choice_dict[index]:
            new_choice = Choice(question=new_question, text=choice)
            new_choice.save()

    return HttpResponseRedirect(reverse('users:own_quizzes', args=(user.username,)))
