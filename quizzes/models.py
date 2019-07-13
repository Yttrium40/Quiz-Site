from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(default=timezone.now, editable=False)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
