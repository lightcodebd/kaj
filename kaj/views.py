from django.shortcuts import render
from kaj.models import JOB, Education_Qualification, JOBLOCATION
# Create your views here.

def kaj_index(request):
    alljob = JOB.objects.all()
    context = {
        'alljob': alljob
    }
    return render(request, 'kaj_index.html', context)

def kaj_detail(request, jobtitle):
    kajdetail = JOB.objects.get(jobtitle=jobtitle)
    context = {
        'kajdetail': kajdetail
    }
    return render(request, 'kaj_detail.html', context)
