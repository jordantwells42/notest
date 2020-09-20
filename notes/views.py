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

def quiz_page(request, username, pk):
    context = None
    if request.method == "POST":
     
        form = request.POST
        questions = {"questions": []}
        for i in range(int(form["qs"])):
            t = random.choice(Term.objects.filter(section__note__id = pk))

            possible_qs = []
            for e in Example.objects.filter(term = t):
                possible_qs.append(e.text)
            for d in Defintion.objects.filter(term = t):
                possible_qs.append(d.text )
            for q in Question.objects.filter(term = t):
                possible_qs.append((q.question, q.answer))

            q = random.choice(possible_qs)
            print(q)
            if type(q) == "Tuple":
                ques = q[0]
                a = q[1]
                w_as = [random.choice(Question.objects.filter(term = t).exclude(answer = a)).answer for j in range(3)]
            elif q:
                ques = f"{q} is a "
                a = t.name
                poss_w_as = []
                for b in Term.objects.exclude(name = t.name):
                    poss_w_as.append(b.name)
                w_as = {random.choice(poss_w_as) for _ in range(3)}
            else:
                continue
            print(a)
            answers = [(a, True)]
            for w_a in w_as:
                answers.append((w_a, False))
            answers = random.shuffle(answers)
            questions['questions'].append({"question": ques, "answer" : answers})
            print(questions)

        context = {
                "questions" : questions,
                "pk": pk,
                "qs" : qs
        }
              

        return render(request, "notes/quiz_page.html", context)

     
def results_page(request, username, pk, qs):
    if request.method == "POST":
        form = request.POST
        correct = 0

        for i in range(1, int(qs) + 1):
            if form[f"answer-{i}"] == "True":
                correct += 1


        context = {
            "correct": correct,
            "qs" : qs,
            "pk" : pk
        }


        return(request, "notes/results_page.html", context)



def notes_index(request, username):
    context = None
    user = User.objects.get(pk = 1)

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
    user = User.objects.get(pk = 1)
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


