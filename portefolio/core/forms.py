
from django import forms
from .models import Contact


class ContatcForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Say Something...'}
        ))
    
    

    class Meta:
        model = Contact
        fields = ['name', 'body', 'email']
