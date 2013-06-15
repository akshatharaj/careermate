from django.forms import ModelForm

from models import Post, PostReport

class PostForm(ModelForm):
    class Meta:
        model = Post

class PostReportForm(ModelForm):
    class Meta:
        model = PostReport
