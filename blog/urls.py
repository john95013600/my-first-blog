from django.conf.urls import url
from . import views


# views.post_list : 使用view.py 的post_list def method去render 頁面
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit ,name='post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish ,name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove ,name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post ,name='add_comment_to_post'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^search/(?P<sd>[\w\-]+)/(?P<ed>[\w\-]+)/(?P<title>[\w\-]+)/$', views.post_search, name='post_search'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/non_approve/$', views.comment_non_approve, name='comment_non_approve'),    
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^google89ddee9020d2d516.html', views.google_search, name='google_search'),
 	url(r'',views.handler404,name='nofound404'),
]

# publist no pk object will return 404
# delete can be done on anomounous account