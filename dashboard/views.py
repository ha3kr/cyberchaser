from django.shortcuts import render, redirect
from .models import Googledorks, Program, Githubdorks, MyNotes, Methodology, Scope
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .core.acquisitions import Acquisitions
from .core.dns import PortScanning
from .core.domains import Domains

# global variables
acq = ''
domain = ''
get_domain = ''
domains = []
subs_db = []
save__option = ''
old_program = ''
org_name = ''
programs = Program.objects.all().order_by('-id')
github_dorks = Githubdorks.objects.all().order_by('-id')
google_dorks = Googledorks.objects.all().order_by('-id')


def check_save(domain_name, field_name, field_value):
    if field_name == "acquisitions":
        if not Program.objects.filter(domain=domain_name).exists():
            Program(ProgramName=program__name, domain=domain_name, acquisitions=field_value).save()
            Message = f"{program__name} Was Added Successfully."
        else:
            Program.objects.filter(domain=domain_name).update(acquisitions=field_value)
            Message = f"{program__name} Has Updated."
    elif field_name == "domains":
        if not Program.objects.filter(domain=domain_name).exists():
            Program(ProgramName=program__name, domain=domain_name, domains=field_value).save()
            Message = f"{program__name} Was Added Successfully."
        else:
            Program.objects.filter(domain=domain_name).update(domains=field_value)
            Message = f"{program__name} Has Updated."
    else:
        Message = ''
    return Message

@login_required
def index(request):
    global domain, acq, domains, Ipv4, programs, program__name, latest_program, get_domain, org_name
    ip_scan_results = ''
    delete_notification = ''
    if request.method == 'POST':
        Message = ''
        domain = request.POST.get('domain')
        program__name = domain.split('.')[0]
        scan_types = request.POST.getlist("scan_types")
        old_program = request.POST.get('old_program')
        save__option = request.POST.get('save__check')
        if len(scan_types) != 0:
            for type in scan_types:
                if type == 'domains':
                    domains, org_name = Domains(domain).get_domains()
                    if save__option == 'save':
                        Message = check_save(domain, "domains", domains)
                elif type == "acq":
                    acq = Acquisitions(domain).result()
                    if save__option == 'save':
                        Message = check_save(domain, "acquisitions", acq)
                elif type == 'git_dork':
                    get_domain = domain
                programs = Program.objects.all().order_by('-id')
            return render(request, 'dashboard/index.html', {'gitdorks': github_dorks, "ggdorks": google_dorks, "acq" : acq, 'domains': domains, 'programs': programs, 'message': Message})
        else:
            get_program = Program.objects.get(id = old_program)
            domain = get_program.ProgramName
            acq = eval(get_program.acquisitions)
            domains  = eval(get_program.domains)
            context = {
                'gitdorks': github_dorks,
                "ggdorks": google_dorks,
                'programs': programs,
                'one_program': get_program,
                'acq': acq.items,
                'domains': domains
            }
            return render(request, "dashboard/index.html", context)

    if request.GET.get('delete'):
        program_id = request.GET.get('delete')
        program_selected = Program.objects.get(id = program_id)
        program_selected_id = program_selected.id
        program_selected_name = program_selected.ProgramName
        Program.objects.get(id=program_selected_id).delete()
        delete_notification = f"{program_selected_name} Deleted Successfully !"
        programs = Program.objects.all()  # update programs table

    if request.GET.get('port_scan'):
        ip = request.GET.get('port_scan')
        ip_scan_results = PortScanning(ip).ScanIP()
    context = {
        'gitdorks': github_dorks,
        "ggdorks": google_dorks,
        "acq" : acq,
        'domains': domains,
        'programs': programs,
        "delete_notification": delete_notification,
        "ip_scan": ip_scan_results
    }
    return render(request, "dashboard/index.html", context)

@login_required
def domains(request):
    global subdomains, domain, domains, org_name
    programs = Program.objects.all()
    if request.method == "POST":
        old_program = Program.objects.get(id=request.POST.get('old__program'))
        domain = old_program.ProgramName
        domains = eval(old_program.domains)
    context = {
        'domain': domain,
        'domains': domains,
        'programs': programs,
        "org_name": org_name
    }
    return render(request, "dashboard/domains.html", context)


@login_required
def scope(request):
    scope_programs = Scope.objects.all()
    if request.GET.get("delete_scope"):
        delete_scope = request.GET.get("delete_scope")
        program_name = Scope.objects.filter(id=delete_scope).get()
        Scope.objects.filter(id=delete_scope).delete()
        Message = f"{program_name.program_name} Scope Deleted !"
        scope_programs = Scope.objects.all()
        return render(request, 'dashboard/my-notes.html', {"scope_programs": scope_programs, "Message": Message})
    if request.method == "POST":
        program_name = request.POST.get('program_name')
        in_scope = request.POST.get('in_scope')
        out_scope = request.POST.get('out_scope')
        Scope(program_name=program_name, in_scope=in_scope, out_scope=out_scope).save()
        messages.success(request, f"{program_name} Scope Added !")
        scope_programs = Scope.objects.all()
    return render(request, "dashboard/scope.html", {"scope_programs": scope_programs})


@login_required
def githubdorks(request):
    get_domain = ''
    github_dorks = Githubdorks.objects.all().order_by('-id')
    if request.method == 'POST':
        if request.POST.get('domain_name'):
            context = {
                "all_dorks": github_dorks,
                "domain": request.POST.get("domain_name")

            }
            return render(request, "dashboard/github-dorks.html", context)
        else:
            dork_name = request.POST.get('dork_name')
            Githubdorks(DorkName=dork_name).save()
            messageSuccess = f"{dork_name} Dork Saved To Database."
            github_dorks = Githubdorks.objects.all().order_by('-id')
            return render(request, "dashboard/github-dorks.html", {'all_dorks': github_dorks, 'domain': get_domain, 'success': messageSuccess})
    return render(request, "dashboard/github-dorks.html")

@login_required
def googledorks(request):
    google_dorks = Googledorks.objects.all().order_by('-id')
    if request.method == "POST":
        if request.POST.get('domain'):
            context = {
                "all_dorks": google_dorks,
                "domain": request.POST.get('domain')
            }
            return render(request, "dashboard/google-dorks.html", context)
        else:
           dork_name = request.POST.get('dork_name')
           dork_desc = request.POST.get('dork_desc')
           Googledorks(dork_name=dork_name, dork_desc=dork_desc).save()
           messageSuccess = f"{dork_name} Dork Saved To Database."
           return render(request, "dashboard/google-dorks.html", {'all_dorks': google_dorks, 'domain': get_domain, 'success': messageSuccess})
    return render(request, "dashboard/google-dorks.html")

@login_required
def acquisitions(request):
    global domain, acq
    if request.method == "POST":
        old_program = Program.objects.get(id=request.POST.get('old__program'))
        domain = old_program.ProgramName
        if not old_program.acquisitions:
            return render(request, 'dashboard/acquisitions.html', {'programs': programs})
        acq = eval(old_program.acquisitions)
        return render(request, 'dashboard/acquisitions.html', {'result': acq.items, 'domain': domain, 'programs': programs})
    if acq: 
        return render(request, 'dashboard/acquisitions.html', {'result': acq.items, 'domain': domain, 'programs': programs})
    return render(request, 'dashboard/acquisitions.html', {'programs': programs})

@login_required
def myNotes(request):
    my_notes = MyNotes.objects.all()
    if request.GET.get("note_id"):
        note_id = request.GET.get("note_id")
        single_note = MyNotes.objects.get(id=note_id)
        context = {
            "all_notes": my_notes,
            "note": single_note
        }
        return render(request, 'dashboard/my-notes.html', context)
    if request.GET.get('delete_note'):
        note_id = request.GET.get('delete_note')
        MyNotes.objects.get(id=note_id).delete()
        my_notes = MyNotes.objects.all()
        context = {
            "all_notes": my_notes,
            "message": "Note Has Been Deleted."
        }
        return render(request, 'dashboard/my-notes.html', context)
    if request.method == "POST":
        noteName = request.POST.get('noteName')
        noteContent = request.POST.get('noteContent')
        MyNotes(note_name=noteName, note_content=noteContent).save()
        my_notes = MyNotes.objects.all()
        context = {
            "all_notes": my_notes,
            "message": "Note Was Added Successfully"
        }
        return render(request, 'dashboard/my-notes.html', context)
    context = {
        "all_notes": my_notes
    }
    return render(request, 'dashboard/my-notes.html', context)

@login_required
def methodology(request):
    if Methodology.objects.count() == 0:
        Methodology(methodology_content="Nothing Yet").save()
        my_methodology = Methodology.objects.all().first()
        record_id = my_methodology.id
    else:
        my_methodology = Methodology.objects.all().first()
        record_id = my_methodology.id
    if request.method == "POST":
        methodology = request.POST.get("methodology_content")
        Methodology.objects.filter(id=record_id).update(methodology_content=methodology)
        messages.success(request, "Methodology Updated !")
        my_methodology = Methodology.objects.all().first()
    return render(request, 'dashboard/methodology.html', {"methodology": my_methodology})


@login_required
def profile(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            User.objects.filter(is_superuser=True).update(username=username)
            u = User.objects.filter(is_superuser=True).get()
            u.set_password(password)
            u.save()
            messages.success(request, "Credentials Changed !")
        elif username:
            User.objects.filter(is_superuser=True).update(username=username)
            messages.success(request, "Username Changed !")
        elif password:
            u = User.objects.filter(is_superuser=True).get()
            u.set_password(password)
            u.save()
            messages.success(request, "Password Changed !")
    return render(request, "dashboard/profile.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect("login:index")
