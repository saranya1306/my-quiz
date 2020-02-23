from .forms import AnswerForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from quiz.models import *

def home(request):
    return render(request,'quiz/home.html',{})

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
        if level_info == 0:
            level_info = 1
        if level_info == 5:
            level_info = 5
        return redirect('get_mcq', level_num=level_info)
    else:
        get_question.is_repeated = True
        get_question.save()
        level_info = score_update.track_score_and_level(get_question.is_correct)
        if level_info == 0:
            level_info = 1
        if level_info == 5:
            level_info = 5
        return redirect('get_mcq', level_num=level_info)

    return True


def get_mcq(request,level_num = None):
    if Questions.objects.filter(is_repeated=True).count() > 10:
        return HttpResponse('<h1>You are done with the Quiz</h1>')
    else:
        score_info = Level.objects.all()
        question = random.choice(Questions.objects.filter(level_no=level_num, is_repeated=False))
        options = Answers.objects.filter(ques=question)
        return render(request, 'quiz/index.html', {'data': options,'ques':question, 'sco':random.choice(score_info)})