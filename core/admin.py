from django.contrib import admin
from core.models import Contact

# @admin.register
# class ContactAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Contact) #, ContactAdmin)
