from .models import Jobs
from django.contrib.auth.decorators import login_required
from .forms import AddjobForm
from userprofile.models import Userprofile
from  django.shortcuts import render, redirect
# Create your views here.

def job_detail(request, job_id):
    job = Jobs.objects.get(pk = job_id)
    return render(request, 'job seeker/detail_jobs.html', {'job':job})

def add_job(request):
    if(request.method == "POST"):
        form = AddjobForm(request.POST)

        if form.is_valid():
            job = form.save(commit= True)
            return redirect('dashboard')
    else:
        form = AddjobForm()
    return render(request, 'job seeker/add_job.html', {'form':form})
