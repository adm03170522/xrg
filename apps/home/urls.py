from django.conf.urls import url
from django.views.static import serve
from xrg.settings import MEDIA_ROOT
from . import views

__author__ = 'Johnny'
__date__ = '2017/10/15 下午8:45'

app_name = 'home'

urlpatterns = [
    # 关于我们
    url(r'^$', views.index, name='index'),
    # 精品课程
    url(r'^course/', views.course, name='course'),
    # 研发团队
    url(r'^teacher/', views.teacher, name='teacher'),
    # 联系我们
    url(r'^contact/', views.contact, name='contact'),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]
