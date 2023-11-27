from django.http import HttpResponse
from .models import Patient
from django.shortcuts import render


def index(request):
    patient_list = Patient.objects.order_by("id")
    context = {"pat_list": patient_list}
    return render(request, "patman/patient_list.html", context)


def detail(request, pat_id):
    patient = Patient.objects.get(id=pat_id)
    context = {'patient': patient}
    return render(request, 'patman/patient_detail.html', context)
