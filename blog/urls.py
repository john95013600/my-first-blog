from django.conf.urls import url
from . import views


# views.post_list : 使用view.py 的post_list def method去render 頁面
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'gg', views.post_gg, name='post_list'),
    # url(r'',views.handler404,name='nofound404'),
]
