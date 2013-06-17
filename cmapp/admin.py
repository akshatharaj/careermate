from django.contrib import admin
from cmapp.models import Post, PostResponse, PostReport

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('post_highlight',)

    def post_highlight(self, obj):
        return ("submitted at %s on '%s at %s' by %s" % (obj.created,
                   obj.job_title, obj.company, obj.author.username))
admin.site.register(Post, PostAdmin)

class PostResponseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('post_response_highlight',)

    def post_response_highlight(self, obj):
        return ("submitted at %s on '%s at %s' by %s" % (obj.created, 
                   obj.post.job_title, obj.post.company, obj.author.username))
admin.site.register(PostResponse, PostResponseAdmin)

class PostReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('post_report_highlight',)

    def post_report_highlight(self, obj):
        return ("submitted at %s on '%s at %s' by %s" % (obj.created, 
                   obj.post.job_title, obj.post.company, obj.author.username))
admin.site.register(PostReport, PostReportAdmin)
