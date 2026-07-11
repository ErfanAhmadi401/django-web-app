from django.contrib import admin
from blog.models import Post

# @admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    empty_value_display = "-empty-"

    """
    fields = [
        "title",
        
    ]
    """

    """
    exclude = [
        content,
        
    ]
    """

    list_display = [
        "title",
        "view_count",
        "status",
        "published_at",

    ]

    list_filter = [
        "status",

    ]

    """
    ordering = [
        "-created_at",

    ]
    """

    search_fields = [
        "title",
        "content",

    ]


admin.site.register(Post, PostAdmin)
