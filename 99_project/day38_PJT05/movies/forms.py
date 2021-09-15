from django import forms 
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        max_length= 100,
        error_messages={
            'required': '내용을 작성해주세요!'
        },
    )
    
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(),   
        error_messages={
            'required': '내용을 작성해주세요!'
        },
    )
    
    poster_path = forms.CharField(
        label='포스터 경로',
        max_length=500,
        error_messages={
            'required': '내용을 작성해주세요!'
        },
    )

    class Meta:
        model = Movie
        fields = '__all__'
        