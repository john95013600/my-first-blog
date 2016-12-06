from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.translation import string_concat
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib import auth
import datetime
import pytz

def about_me(request):
    return render(request,'blog/about_me.html')

# post 查詢詳細貼文屬性資料
def post_search(request, sd, ed, title):
    naive_sd = datetime.datetime.strptime(sd, '%Y-%m-%d')
    start_date = pytz.timezone('Asia/Taipei').localize(naive_sd)
    naive_ed = datetime.datetime.strptime(ed, '%Y-%m-%d')
    end_date = pytz.timezone('Asia/Taipei').localize(naive_ed)
    posts = Post.objects.filter(published_date__range=(start_date, end_date)).filter(title__icontains=title).order_by('-published_date')
    postall = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    classify = Post.objects.order_by('post_type')
    return render(request, 'blog/post_list.html', {'posts': posts, 'postall': postall, 'class': classify})

# post  有published_date的貼文
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postall = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    classify = Post.objects.order_by('post_type')
    return render(request, 'blog/post_list.html', {'posts': posts, 'postall': postall, 'class': classify})


# 當404 Page not found時顯示
def handler404(request):
    return render(request,'blog/404.html')

def post_detail(request, pk):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    classify = Post.objects.order_by('post_type')
    try:
        # post = get_object_or_404(Post, pk=pk)
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        post = None
    if post != None:
        return render(request, 'blog/post_detail.html', {'post': post,'postall': posts, 'class': classify})
    else:
        return redirect('nofound404')

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.author = request.user
		    # post.published_date = timezone.now()
		    # published_date 不應該改
            # post.post_url = post.post_url
		    post.save()
		    return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            # published_date 不應該改
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# post  有created_date的貼文
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=post.pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.approved_comment = True
            comment.save()

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_non_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.non_approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

def google_search(request):
    return render(request, 'blog/google89ddee9020d2d516.html')


