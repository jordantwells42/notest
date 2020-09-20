from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Note(models.Model):
	title = models.CharField(max_length = 255)
	created_on = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
	tags = models.ManyToManyField('tag', related_name='notes')

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=35)
	def __str__(self):
		return self.name

class Section(models.Model):
	title = models.CharField(max_length = 255)
	note = models.ForeignKey(Note, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Term(models.Model):
	name = models.CharField(max_length = 255)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Example(models.Model):
	text = models.CharField(max_length = 255)
	term = models.ForeignKey(Term, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class Definition(models.Model):
	text = models.CharField(max_length = 255)
	term = models.ForeignKey(Term, on_delete=models.CASCADE)

	def __str__(self):
		return self.text


class Question(models.Model):
	question = models.CharField(max_length = 255)
	answer = models.CharField(max_length = 255)
	term = models.ForeignKey(Term, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.question}: {self.answer}"


"""
class Result(models.Model):
	correct = models.IntegerField()
	total = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.correct}/{self.correct}"
"""
