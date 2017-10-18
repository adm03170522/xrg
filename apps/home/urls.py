from django.conf.urls import url
from . import views

__author__ = 'Johnny'
__date__ = '2017/10/15 下午8:45'

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^course/', views.course, name='course'),
    url(r'teacher/', views.teacher, name='teacher'),
    url(r'contact/', views.contact, name='contact')
]
