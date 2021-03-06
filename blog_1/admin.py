from django.contrib import admin
from .models import Blog, PersonalBlog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register((Blog, PersonalBlog), BlogAdmin)