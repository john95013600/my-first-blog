from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    post_url = models.URLField(blank=True, default='http://john95013600.pythonanywhere.com/')
    post_type = models.CharField(max_length=50, default='Life')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title
# published_date 只有在第一次被publish時改變
# 新增 last_edited_date

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200, default='Visitor')
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def non_approve(self):
        self.approved_comment = False
        self.save()

    def __str__(self):
        return self.text
