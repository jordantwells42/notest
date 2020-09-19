from django.shortcuts import render, redirect
from django.core import serializers
from .models import *
from .serializers import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework import permissions
import json
import random

# Create your views here.
def quiz_page(request, username, pk, qs):
	context = None
	questions = {}
	for i in range(qs):
		t = random.choice(Term.objects.filter(section__note__id = pk))

		possible_qs = []

		possible_qs.append([e.text for e in Example.objects.filter(term = t)])
		possible_qs.append([d.text for d in Defintion.objects.filter(term = t)])
        possible_qs.append([(q.question, q.answer) for q in Question.objects.filter(term = t)])


        q = random.choice(possible_questions)

        if len(q) == 2:
        	question = q[0]
        	answer = q[1]
        else:
        	question = q
        	answer = t.term_name

        questions.update(question = answer)
        
    context = {
    	"questions" : questions
    }	

    return redirect



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
			note = {}
			note["sections"] = []
			for i, s in enumerate(Section.objects.filter(note__id = pk)):
				note["sections"].append({})
				note["sections"][i]["section_title"] = s.title
				note["sections"][i]["terms"] = []
				for j, t in enumerate(Term.objects.filter(section  = s)):
					note["sections"][i]["terms"].append({})
					note["sections"][i]["terms"][j]["term_name"] = t.name

					
					note["sections"][i]["terms"][j]["defintions"] = [d.text for d in Defintion.objects.filter(term = t)]

				
					note["sections"][i]["terms"][j]["examples"] = [e.text for e in Example.objects.filter(term = t)]


					note["sections"][i]["terms"][j]["questions"] = [q.text for q in Question.objects.filter(term = t)]
			
			print(note)
			context = {
				"notes": note,
				"note": n
			}



			return render(request, "notes/note_page.html", context)

		else:
			return redirect("notes:notes_index", user.get_username())

	else:
		return redirect("login")


