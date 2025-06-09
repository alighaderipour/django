from django.shortcuts import render
from .models import  JobPosting
# Create your views here.
def index(request):
    job_postings = JobPosting.objects.all()
    active_job_postings = JobPosting.objects.filter(is_active=True)
    not_active_job_postings = JobPosting.objects.filter(is_active=False)
    print(job_postings)
    context = {'job_postings': job_postings, 'not_active_job_postings': not_active_job_postings, 'active_job_postings': active_job_postings}
    return render(request, 'job_board/index.html', context)

def job_details(request, job_id):
    job = JobPosting.objects.get(id=job_id)
    context = {'job': job}
    return render(request, 'job_board/job_detail.html', context)