from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_gg(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/gg.html', {'posts': posts})

# handler404 = 'views.handler404'

def handler404(request):
     return render(request,'blog/404.html')