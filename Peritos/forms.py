from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'col s12 m6 14'}))
    password = forms.CharField(widget=forms.PasswordInput())