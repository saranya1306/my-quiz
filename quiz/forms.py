from django import forms

from .models import *

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ('ques', 'answer_options',)