from django.contrib import admin
from website.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'subject', 'content', 'email']

admin.site.register(Contact, ContactAdmin)