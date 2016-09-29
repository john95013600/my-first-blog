from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import PostForm

from .models import Post
# post  有published_date的貼文
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# post  有created_date的貼文
def post_gg(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# 當404 Page not found時顯示
def handler404(request):
    return render(request,'blog/404.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.author = request.user
		    post.published_date = timezone.now()
		    # published_date 不應該改
		    post.save()
		    return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # published_date 不應該改
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})