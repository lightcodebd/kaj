from django.shortcuts import render
from kaj.models import JOB, Education_Qualification, JOBLOCATION
# Create your views here.

def kaj_index(request):
    alljob = JOB.objects.all()
    context = {
        'alljob': alljob
    }
    return render(request, 'kaj_index.html', context)


def kaj_detail(request, pk):
    kajdetail = JOB.objects.get(pk=pk)
    context = {
        'kajdetail': kajdetail
    }
    return render(request, 'kaj_detail.html', context)

def kaj_findbyqualification(request, education_qualification):
#    kajdetail = JOB.objects.get(jobtitle=jobtitle)
    find = Education_Qualification.objects.get(examname=education_qualification)
    kajqualification = JOB.objects.filter(education_qualification=find.pk)
    context = {
        'kajqualification': kajqualification
    }
    return render(request, 'kaj_findbyqualification.html', context)
