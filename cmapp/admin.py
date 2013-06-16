from django.contrib import admin
from cmapp.models import Post, PostResponse, PostReport

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)

class PostResponseAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostResponse, PostResponseAdmin)

class PostReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostReport, PostReportAdmin)
