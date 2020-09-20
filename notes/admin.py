from django.contrib import admin
from .models import *

class NoteAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class SectionAdmin(admin.ModelAdmin):
    pass

class TermAdmin(admin.ModelAdmin):
    pass

class ExampleAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
	pass

class DefinitionAdmin(admin.ModelAdmin):
	pass


#class ResultAdmin(admin.ModelAdmin):
#	pass


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Definition, DefinitionAdmin)
#admin.site.register(Result, ResultAdmin)