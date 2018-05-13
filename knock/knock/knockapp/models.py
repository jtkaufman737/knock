from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # Change later if need be. 'recent' is so subjective
        return self.pub_date >= timezone.now - datetime.timedelta(days=7)

class Punchline(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Remember this from Ruby, destroying child db object
    punchline_text = models.CharField(max_length=500)

    def __str__(self):
        return self.punchline_text
