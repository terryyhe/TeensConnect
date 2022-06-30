from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "firstname", "lastname", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        
        if commit:
            user.save()
        return user