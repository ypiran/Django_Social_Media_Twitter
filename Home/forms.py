from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('body', 'post_image')
      widgets = {
         'body': forms.Textarea(attrs={'class': 'form-control'}),
      }

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels ={
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment...'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment...', 'style': 'width:50%;height:100px;'})
        }