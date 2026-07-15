from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Post(models.Model):
    image = models.ImageField(upload_to="blog/", default="blog/dedault.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # tag_id
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = [
        #     "-created_at",

        # ]

        # verbose_name = "POST"
        # verbose_name_plural = "POSTS"

        """
            abstract
            verbose_name
            verbose_name_plural
            app_label
            ordering
            proxy
            permissions

        """

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
