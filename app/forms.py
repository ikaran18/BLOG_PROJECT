from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['title','author','content',]
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type' :'hidden'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name','body',]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }