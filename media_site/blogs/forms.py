from django import forms
from blogs.models import Submission


class PostForm(forms.Form):
    post_title = forms.CharField(label="Post title", max_length=30)
    post_content = forms.CharField(label="Post content", max_length=300, widget=forms.Textarea)


class PostFormFromModel(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'content', 'pub_date', 'user']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=40, label="Subject:")
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
