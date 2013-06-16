from django.forms import ModelForm
from django import forms
from models import Post, PostReport, PostResponse

from constants import SEARCH_BY_CHOICES

class PostForm(ModelForm):
    class Meta:
        model = Post

class PostSearchForm(forms.Form):
    search_by = forms.ChoiceField(choices=SEARCH_BY_CHOICES)
    search_text = forms.CharField(min_length=3, required=True)

class PostReportForm(ModelForm):
    class Meta:
        model = PostReport    

class PostResponseForm(ModelForm):
    class Meta:
        model = PostResponse

