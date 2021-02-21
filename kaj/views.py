from django.shortcuts import render
from kaj.models import JOB
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
