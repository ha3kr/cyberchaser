from csv import list_dialects
from django.contrib import admin
from .models import Program, Githubdorks, Googledorks, MyNotes, Methodology, Scope


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProgramName', 'domain', 'domains', 'acquisitions', 'start_date')

class GithubDorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'DorkName')

class GoogleDorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'dork_name', 'dork_desc')

class MyNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'note_name', 'note_content', 'note_date')

class MethodologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'methodology_content')

class ScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'program_name', "in_scope", "out_scope")


admin.site.register(Program, ProgramAdmin)
admin.site.register(Githubdorks, GithubDorkAdmin)
admin.site.register(Googledorks, GoogleDorkAdmin)
admin.site.register(MyNotes, MyNotesAdmin)
admin.site.register(Methodology, MethodologyAdmin)
admin.site.register(Scope, ScopeAdmin)