from django.http import HttpResponse
from .models import Patient
from django.shortcuts import render, redirect

def index(request):
    patient_list = Patient.objects.order_by('patient_id')
    context = {'pat_list': patient_list}
    return render(request, 'patman/patient_list.html', context)

def detail(request, pat_id):
    patient = Patient.objects.get(id=pat_id)
    context = {'patient': patient}
    return render(request, 'patman/patient_detail.html', context)


def learn_html(request):
    return render(request, 'patman/learn_html.html')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = Patient.objects.get(patient_id=username)
        if me.patient_pw == password:
            request.session['user'] = me.username
            return HttpResponse(f"로그인 성공! {me.username}님 환영합니다!")
        else:
            return redirect('/patman/sign_in')
    elif request.method == 'GET':
        return render(request, 'user/sign-in.html')

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/sign-up.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        patient_name = request.POST.get('name', None)
        patient_birthday = request.POST.get('birthday', None)
        patient_tel = request.POST.get('tel', None)
        patient_home = request.POST.get('home', None)
        patient_accept_id = request.POST.get('accept_id', None)
        patient_hos = request.POST.get('hos', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/sign-up.html')
        else:
            exist_user = Patient.objects.filter(patient_id=username)
            if exist_user:
                return render(request, 'user/sign-up.html')
            else:
                new_user = Patient()
                new_user.patient_id = username
                new_user.patient_name = patient_name
                new_user.patient_birthday = patient_birthday
                new_user.patient_tel = patient_tel
                new_user.patient_gender = bio
                new_user.patient_home = patient_home
                new_user.patient_accept_id = patient_accept_id
                new_user.patient_hos = patient_hos
                new_user.patient_pw = password
                new_user.save()
                return redirect('/patman/sign_in')
