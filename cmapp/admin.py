from django.contrib import admin
from cmapp.models import Post

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
