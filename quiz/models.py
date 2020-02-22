from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length = 200, null = False,blank = False)
    level = models.IntegerField(default=1,null = False,blank = False)

    def __str__(self):
        return self.question


class Answers(models.Model):
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_options = models.CharField(max_length=100,blank = False)
    right_answer = models.CharField(max_length=100,blank = False)
    is_repeated = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a repeated question?")
    is_correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?")

    def __str__(self):
        return self.ques.question + '_' + self.answer_options

class Level(models.Model):
    mcq = models.ForeignKey(Answers, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    level_flag = models.IntegerField(default = 1)

    def check_if_correct(self):
        if self.mcq.is_correct is True:
            self.score = self.score + 1
            self.level_flag = self.level_flag + 1
            return self.level_flag
        else:
            self.score = self.score
            self.level_flag = self.level_flag - 1
            return self.level_flag

    def __str__(self):
        return str(self.score)

