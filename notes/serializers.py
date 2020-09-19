from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'title', 'sections']

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['title', 'terms']

class TermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Term
        fields = ['name', 'defintions', 'examples', 'questions']


