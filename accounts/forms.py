from django import forms
from .models import User
class Register_form(forms.ModelForm):
    username = forms.TextInput()
    email = forms.EmailField()
    attrs = {
        "type": "password",
        'autocomplete':'off'
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
    class Meta:
        model = User
        fields = ['username','email','password']
        

class Login_form(forms.Form):
    pass
