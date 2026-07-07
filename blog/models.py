from django.db import models

class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category_id
    # tag_id
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    