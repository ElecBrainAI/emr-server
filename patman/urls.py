from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework import routers
app_name = 'patman'
router = routers.DefaultRouter()
router.register('users', views.PatientViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pat_id>/', views.detail, name='detail'),
    path('learn_html/', views.learn_html, name='learn_html'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('api/', include(router.urls))
]