from django.conf.urls import url
from . import views


# views.post_list : 使用view.py 的post_list def method去render 頁面
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit ,name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    url(r'gg', views.post_gg, name='post_list'),
    url(r'',views.handler404,name='nofound404'),
]
