from django.shortcuts import render, redirect
from django.core import serializers
from .models import *
from django.contrib.auth import *

# Create your views here.
def notes_index(request, username):
	context = None
	user = request.user
	print(username)
	if user.is_authenticated and user.get_username() == username:
		notes = Note.objects.filter(user=user)


		context = {
			"notes" : notes
		}

		return render(request, "notes/notes_index.html", context)

	else:
		return redirect("login")

def note_page(request, username, pk):
	context = None
	user = request.user
	if user.is_authenticated and user.get_username() == username:
		if pk in [note.id for note in Note.objects.filter(user=user)]:
			n = Note.objects.get(pk = pk)

			"""
			note = {}
			for s in Section.objects.filter(note = n):
				note.update(s = {})
				for t in Term.objects.filter(section  = s):
					for d in Defintion.objects.filter(term = t):


					for e in Example.objects.filter(term = t):

					for q in Question.objects.filter(term = q):

			"""

			note = serializers.serialize('json', Note.objects.get(pk = pk), handle_forward_references=True)
			print(note)
			context = {
				"sections" : [section for section in Section.objects.filter(note = n)]
			}



			return render(request, "notes/note_page.html", context)

		else:
			return redirect("notes:notes_index", user.get_username())

	else:
		return redirect("login")