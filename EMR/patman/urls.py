from django.urls import path
from . import views

app_name = 'patman'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pat_id>/', views.detail, name='detail')
]
