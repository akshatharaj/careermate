from django.contrib import admin
from django.core.urlresolvers import reverse

from models import Post, PostResponse, PostReport
from utils import accept_post_reports

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('id', 'post_highlight',)

    def post_highlight(self, obj):
        return ("submitted at %s on '%s at %s' by %s" % (obj.created,
                   obj.job_title, obj.company, obj.author.username))
admin.site.register(Post, PostAdmin)

class PostResponseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('parent_post_id', 'post_response_highlight',)

    def parent_post_id(self, obj):
        return obj.post.id

    def post_response_highlight(self, obj):
        return ("%s's response to '%s at %s' on %s" % (obj.author.username,
                   obj.post.job_title, obj.post.company, obj.created.date()))
admin.site.register(PostResponse, PostResponseAdmin)

class PostReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    actions = ['accept_report']
    list_display = ('parent_post_id', 'post_report_highlight',)

    def parent_post_id(self, obj):
        return obj.post.id

    def post_report_highlight(self, obj):
        return ("%s reported '%s at %s' on %s" % (obj.author.username,
                   obj.post.job_title, obj.post.company, obj.created.date()))

    def accept_report(self, request, queryset):
        posts = queryset.values_list('post_id', flat=True)
        accept_post_reports(queryset)
        self.message_user(request, 
                          '%d post(s) were taken offline as a result of this action' % len(posts))
    accept_report.short_description = 'Accept report and take related post offline'

    def change_view(self, request, object_id, extra_context=None):
        actions = self.get_actions(request)
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_action_choices(request)
        else:
            action_form = None
        changelist_url = reverse('admin:cmapp_postreport_changelist')
        return super(PostReportAdmin, self).change_view(request, object_id, extra_context={
            'action_form': action_form,
            'changelist_url': changelist_url
        })

admin.site.register(PostReport, PostReportAdmin)
