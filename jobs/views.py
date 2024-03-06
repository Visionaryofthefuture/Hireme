from .models import Jobs
from django.contrib.auth.decorators import login_required
from .forms import *
from userprofile.models import Userprofile
from  django.shortcuts import render, redirect

# Create your views here.

def job_detail(request, job_id):
    job = Jobs.objects.get(pk = job_id)
    return render(request, 'job seeker/detail_jobs.html', {'job':job})

@login_required
def add_job(request):
    if(request.method == "POST"):
        form = AddjobForm(request.POST, request.FILES)
        print(form.errors)

        if form.is_valid():
            job = form.save(commit= False)
            job.recruiter = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = AddjobForm()
    return render(request, 'job seeker/add_job.html', {'form':form})


@login_required
def apply_for_job(request, job_id):
    job = Jobs.objects.get(pk = job_id)
    if(request.method == "POST"):
        form = ApplicationForm(request.POST)
        if(form.is_valid()):
            application = form.save(commit = False)
            application.job = job
            application.created_by = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, "job seeker/apply_for_job.html", {'form': form, 'job': job})


