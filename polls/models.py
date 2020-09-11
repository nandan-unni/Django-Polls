import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question_text
    def is_new(self):
        return self.mod_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    no_of_votes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return '{} ({})'.format(self.choice_text, self.question.question_text)
