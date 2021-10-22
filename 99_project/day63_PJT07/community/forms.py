from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    movie_title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'})
    )
    
    class Meta:
        model = Review
        fields = ('title', 'movie_title', 'content', 'rank',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2,
        max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        fields = ('content', )