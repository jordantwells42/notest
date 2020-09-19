from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Example(models.Model):
	text = models.CharField(max_length = 255)


	def __str__(self):
		return self.text

class Defintion(models.Model):
	text = models.CharField(max_length = 255)

	def __str__(self):
		return self.text


class Question(models.Model):
	question = models.CharField(max_length = 255)
	answer = models.CharField(max_length = 255)
	

	def __str__(self):
		return f"{self.question}: {self.answer}"

class Term(models.Model):
	name = models.CharField(max_length = 255)
	examples = models.ManyToManyField(Example, related_name = 'terms')
	definitions = models.ManyToManyField(Defintion, related_name = 'terms')
	questions = models.ManyToManyField(Question, related_name = 'terms')

	def __str__(self):
		return self.name


class Section(models.Model):
	title = models.CharField(max_length = 255)
	terms = models.ManyToManyField(Term, related_name = 'sections')

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=20)


class Note(models.Model):
	title = models.CharField(max_length = 255)
	created_on = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
	tags = models.ManyToManyField('tag', related_name='notes')
	sections = models.ManyToManyField(Section, related_name = 'notes')

	def __str__(self):
		return self.title










