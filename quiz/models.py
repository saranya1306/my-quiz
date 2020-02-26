from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

LEVEL_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class PopulateData(models.Model):
    my_file = models.FileField(upload_to='files/', max_length=254)
    # created_datetime = models.DateTimeField(default=datetime.now)

    def save(self, *args,**kwargs):
        all_files = glob.glob("media/files/*")
        latest_file = max(all_files, key=os.path.getctime)
        with open(latest_file) as f:
            lis = [line.split() for line in f]        # create a list of lists
            for i, x in enumerate(lis):              #print the list items 
                category,que,ans1,ans2,ans3,ans4,answ_true = x[0].split(",")
                cat = Category.objects.create(category_name=category)
                ques = Questions.objects.create(category_type=cat,question=que)
                Answers.objects.create(ques=ques,answer_options=ans1,right_answer=answ_true)
                Answers.objects.create(ques=ques,answer_options=ans2,right_answer=answ_true)
                Answers.objects.create(ques=ques,answer_options=ans3,right_answer=answ_true)
                Answers.objects.create(ques=ques,answer_options=ans4,right_answer=answ_true)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Questions(models.Model):
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length = 200, null = False,blank = False)
    level_no = models.IntegerField(choices=LEVEL_CHOICES,default = 1,blank=True)
    is_repeated = models.BooleanField(blank=False,
                                default=False,
                                help_text="Is this a repeated question?")
    is_correct = models.BooleanField(blank=False,
                                default=False,
                                help_text="Is this a correct answer?")



    def __str__(self):
        return self.question + str(self.level_no)


class Answers(models.Model):
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_options = models.CharField(max_length=100,blank = False)
    right_answer = models.CharField(max_length=100,blank = False)


    def __str__(self):
        return self.ques.question + '_' + self.answer_options

class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0,null=True,validators=[MinValueValidator(0), MaxValueValidator(100)])
    level_flag = models.PositiveIntegerField(default=1,null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(6)])

    # def track_score_and_level(self,is_correct):
    #     if is_correct is True:
    #         self.score = self.score + 1
    #         self.level_flag = self.level_flag + 1
    #         self.save()
    #         return self.level_flag
    #     else:
    #         self.score = self.score
    #         self.level_flag = self.level_flag - 1
    #         self.save()
    #         return self.level_flag

    def __str__(self):
        return str(self.score)

