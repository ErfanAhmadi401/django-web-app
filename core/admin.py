from django.contrib import admin
from core.models import Contact

# @admin.register


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    
    list_display = [
        "name",
        "email",
        "created_at",
        
    ]
    
    list_filter = [
        "email",
        
    ]
    
    search_fields = [
        "name",
        "message",
        
    ]


admin.site.register(Contact, ContactAdmin)
