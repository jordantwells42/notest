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
        for i in range(int(form.get("qs"))):
            t = random.choice(Term.objects.filter(section__note__id = pk))

            possible_qs = []
            for e in Example.objects.filter(term = t):
                possible_qs.append(e.text)
            for d in Definition.objects.filter(term = t):
                possible_qs.append(d.text )
            for q in Question.objects.filter(term = t):
                possible_qs.append((q.question, q.answer))
            if len(possible_qs) == 0:
                continue
                
            q = random.choice(possible_qs)
            print(q)
            if type(q) == "Tuple":
                ques = q[0]
                a = q[1]
                w_as = [random.choice(Question.objects.filter(term = t).exclude(answer = a)).answer for j in range(3)]
            elif q:
                ques = f"{q}"
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
            random.shuffle(answers)
            questions['questions'].append({"question": ques, "answer" : answers})
            print(questions)
            print(answers)

        context = {
                "questions" : questions,
                "pk": pk,
                "qs" : int(form["qs"])
        }
              

        return render(request, "notes/quiz_page.html", context)

     
def results_page(request, username, pk, qs):
    if request.method == "POST":
        form = request.POST
        print(form)
        correct = 0

        for i in range(1, int(qs) + 1):
            if form.get(f"answer-{i}") == "True":
                correct += 1


        context = {
            "correct": correct,
            "qs" : qs,
            "pk" : pk
        }

        #result = Result(correct = correct, total = qs, note = Note.objects.get(pk = pk))
        #result.save()

        return render(request, "notes/results_page.html", context)



def notes_index(request, username):
    if request.method == "POST":
        form = request.POST
        n = Note(title = form.get("title"), user = request.user)
        n.save()

    context = None
    user = request.user

    if user.is_authenticated and user.get_username() == username:
        notes = Note.objects.filter(user=user)

        context = {
            "notes" : notes
        }

        return render(request, "notes/notes_index.html", context)

    else:
        return redirect("login")

def note_page(request, username, pk):
    if request.method == "POST":
        form = request.POST

        text = form.get("text")
        model = form.get("model")
        parent = form.get("parent")
        n = Note.objects.get(pk = pk)

        if model == "Section":
            s = Section(title = text, note = n)
            s.save()
        if model == "Term":
            t = Term(name = text, section = Section.objects.filter(title__icontains = parent).first())
            t.save()
        if model == "Definition":
            d = Definition(text = text, term = Term.objects.filter(name__icontains = parent).first())
            d.save()
        if model == "Example":
            e = Example(text = text, term = Term.objects.filter(name__icontains = parent).first())
            e.save()
        

    context = None
    user = request.user
    if user.is_authenticated and user.get_username() == username:
        if pk in [note.id for note in Note.objects.filter(user=user)]:
            n = Note.objects.get(pk = pk)
            # print(Result.objects.filter(note = n))

            note = {}
            note["sections"] = []
            for i, s in enumerate(Section.objects.filter(note__id = pk)):
                note["sections"].append({})
                note["sections"][i]["section_title"] = s.title
                note["sections"][i]["terms"] = []
                for j, t in enumerate(Term.objects.filter(section  = s)):
                    note["sections"][i]["terms"].append({})
                    note["sections"][i]["terms"][j]["term_name"] = t.name

                    
                    note["sections"][i]["terms"][j]["definitions"] = [d.text for d in Definition.objects.filter(term = t)]

                
                    note["sections"][i]["terms"][j]["examples"] = [e.text for e in Example.objects.filter(term = t)]


                    note["sections"][i]["terms"][j]["questions"] = [q.text for q in Question.objects.filter(term = t)]
            

            context = {
                "notes": note,
                "note": n,
                #"results": results
            }



            return render(request, "notes/note_page.html", context)

        else:
            return redirect("notes:notes_index", user.get_username())

    else:
        return redirect("login")



        



