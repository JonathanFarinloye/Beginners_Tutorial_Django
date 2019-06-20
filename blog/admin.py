from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'cover', 'slug')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Blog, BlogAdmin)