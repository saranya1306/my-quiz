from .forms import AnswerForm
from django.shortcuts import render,redirect
import random
from quiz.models import *


def validate_mcq(request,question_id = None):
    print("in the main")
    score_update = Level.objects.get(id=1)
    # if request.method == "POST":
    print("In Post method")
    get_question = Questions.objects.get(id = question_id)
    get_answer = Answers.objects.filter(ques=get_question)
    user_response = request.POST.get("answer")
    if random.choice(get_answer).right_answer == user_response:
        print("In Validation")
        get_question.is_repeated = True
        get_question.is_correct = True
        get_question.save()
        level_info = score_update.track_score_and_level(get_question.is_correct)

        # if questions is repeated=false is 10 then tell it's done and display the score else share the level info
        return redirect('get_mcq', level_num=level_info)
    else:
        get_question.is_repeated = True
        get_question.save()
        level_info = score_update.track_score_and_level(get_question.is_correct)

        # if questions is repeated=false is 10 then tell it's done and display the score else share the level info
        return redirect('get_mcq', level_num=level_info)

    return True


def get_mcq(request,level_num = None):
    score_info = Level.objects.all()
    question = random.choice(Questions.objects.filter(level_no=level_num, is_repeated=False))
    options = Answers.objects.filter(ques=question)
    return render(request, 'quiz/index.html', {'data': options,'ques':question, 'score':score_info})