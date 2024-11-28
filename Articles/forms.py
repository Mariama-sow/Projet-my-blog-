from django import forms
from django.contrib.auth.models import User
from .models import Articles , Comment 

# class ArticlesForm(forms.Form) :
#     title = forms.CharField(min_length=2 , max_length=255)
#     sumary = forms.CharField(min_length=2 , max_length=255 ,required=False)
#     date_pub = forms.DateField(required=False)
#     content = forms.CharField(widget=forms.Textarea(attrs={'required':True}))


class ArticlesForm(forms.ModelForm) :
    cover = forms.ImageField(required=True)

    
    class Meta:
        model = Articles
        fields = ('title','sumary','date_pub','content','cover','categorie')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titre'}),
            'sumary' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'resume'}),
            'date_pub' : forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':'Date de publication'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder':'contenu'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control' , 'placeholder':'votre commentaire'})
        }

