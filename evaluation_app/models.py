from django.db import models


# Create your models here.
class AnswerList(models.Model):
    evaluator = models.CharField(max_length=300)
    evaluated_person = models.CharField(max_length=100)
    email_evaluator = models.EmailField()
    answers = models.CharField(max_length=200)
    Q1 = models.FloatField()
    Q2 = models.FloatField()
    Q3 = models.FloatField()
    Q4 = models.FloatField()
    C1 = models.FloatField()
    C2 = models.FloatField()
    C3 = models.FloatField()
    C4 = models.FloatField()
    C5 = models.FloatField()
    C6 = models.FloatField()
    C7 = models.FloatField()
    C8 = models.FloatField()
    category_answer = models.CharField(max_length=100)
    answer_date = models.DateTimeField()
    leader = models.CharField(max_length=70)
    comment_1 = models.CharField(max_length=1000)
    comment_2 = models.CharField(max_length=1000)
