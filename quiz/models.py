from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

LEVEL_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class CategorY(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Questions(models.Model):

    question = models.CharField(max_length = 200, null = False,blank = False)
    level_no = models.IntegerField(choices=LEVEL_CHOICES,default = 1,blank=True)
    is_repeated = models.BooleanField(blank=False,
                                default=False,
                                help_text="Is this a repeated question?")
    is_correct = models.BooleanField(blank=False,
                                default=False,
                                help_text="Is this a correct answer?")



    def __str__(self):
        return self.question


class Answers(models.Model):
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_options = models.CharField(max_length=100,blank = False)
    right_answer = models.CharField(max_length=100,blank = False)


    def __str__(self):
        return self.ques.question + '_' + self.answer_options

class Level(models.Model):
    # Add a user_id field will be linked to this
    score = models.PositiveIntegerField(default = 0,blank=True,validators=[MinValueValidator(0), MaxValueValidator(100)])
    level_flag = models.PositiveIntegerField(default=1,blank = False,validators=[MinValueValidator(0), MaxValueValidator(6)])

    def track_score_and_level(self,is_correct):
        if is_correct is True:
            self.score = self.score + 1
            self.level_flag = self.level_flag + 1
            self.save()
            return self.level_flag
        else:
            self.score = self.score
            self.level_flag = self.level_flag - 1
            self.save()
            return self.level_flag

    def __str__(self):
        return str(self.score)

