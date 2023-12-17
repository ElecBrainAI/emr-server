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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt  # CSRF 토큰 검사 비활성화 (개발 시에만)
def sign_in_view(request):
    if request.method == 'POST':
            data = json.loads(request.body)
            print(data)
            username = data['username']
            password = data['password']

            me = Patient.objects.get(patient_id=username)
            if me.patient_pw == password:
                request.session['user'] = me.patient_id
                print(1)# 로그인 성공 시
                return JsonResponse({'message': '로그인 성공'})

            else:
                print(2)
                return JsonResponse({'message': '로그인 실패'}, status=401)


@csrf_exempt
def sign_up_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data['username']
        password = data['password']
        password2 = data['password2']
        patient_name = data['name']
        patient_birthday = data['birth']
        patient_tel = data['tel']
        patient_home = data['home']
        patient_accept_id = data['parent']
        bio = data['bio']

        if patient_accept_id == '' or patient_accept_id == "null":
            patient_accept_id = " "
        if password != password2:
            JsonResponse({'message': '회원가입 실패'}, status=401)
        else:
            exist_user = Patient.objects.filter(patient_id=username)
            if exist_user:
                return JsonResponse({'message': '이미 존재하는 회원'}, status=401)
            else:
                new_user = Patient()
                new_user.patient_id = username
                new_user.patient_name = patient_name
                new_user.patient_birthday = patient_birthday
                new_user.patient_tel = patient_tel
                new_user.patient_gender = bio
                new_user.patient_home = patient_home
                new_user.patient_accept_id = patient_accept_id
                new_user.patient_hos = 1
                new_user.patient_pw = password
                new_user.save()
                print(1)
                return JsonResponse({'message': '회원가입 성공'})



from rest_framework import viewsets
from .serializers import PatientSerializer
from .models import Patient

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer