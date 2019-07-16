from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Quiz(models.Model):
    author = models.ForeignKey(User, related_name='authored_set', on_delete=models.PROTECT)
    name = models.CharField(default="My Quiz", max_length=50)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    taken_by = models.ManyToManyField(User, related_name='taken_set')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
