from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

class Punchline(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Remember this from Ruby, destroying child db object
    punchline_text = models.CharField(max_length=500)
