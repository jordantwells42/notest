from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("<str:username>/", views.notes_index, name = "notes_index"),
    path("<str:username>/<int:pk>/", views.note_page, name = "note_page"),
    path("<str:username>/<int:pk>/quiz/", views.quiz_page, name = "quiz_page"),
    path("<str:username>/<int:pk>/quiz/result/<int:qs>", views.results_page, name = "result_page"),
] 

app_name = "notes"