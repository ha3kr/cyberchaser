from django.db import models
import datetime

class Program(models.Model):
    def __str__(self):
        return self.ProgramName
    ProgramName = models.CharField(max_length=30, default="program name")
    domain = models.CharField(max_length=30, default="domain name")
    domains = models.TextField(default="Domains Related")
    acquisitions = models.TextField(default="Companies Accuired.")
    start_date = datetime.date.today()

class Githubdorks(models.Model):
    def __str__(self):
        return self.DorkName
    DorkName = models.CharField(max_length=30, default="Dork Name")

class Googledorks(models.Model):
    def __str__(self):
        return self.dork_name
    dork_name = models.CharField(max_length=30, default="Dork Name")
    dork_desc = models.CharField(max_length=40, default="Dork description")

class MyNotes(models.Model):
    def __str__(self):
        return self.note_name
    note_name    = models.CharField(max_length=30, default="Note Name")
    note_content = models.TextField(default="Note description")
    note_date = datetime.date.today()

class Methodology(models.Model):
    methodology_content = models.TextField(default="No Methodology Yet !")

class Scope(models.Model):
    def __str__(self):
        return self.program_name
    program_name = models.CharField(max_length=20, default="Program Name")
    in_scope = models.TextField(default="in scope")
    out_scope = models.TextField(default="out scope")
