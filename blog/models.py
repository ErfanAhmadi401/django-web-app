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
    
    class Meta:
        ordering = [
            "-created_at",
            
        ]
        
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
