from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("<str:username>/", views.notes_index, name = "notes_index"),
    path("<str:username>/<int:pk>", views.note_page, name = "note_page"),
    path("notes", views.NoteSerializer)
] 

app_name = "notes"