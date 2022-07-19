from django import forms
from django.contrib.auth.forms import UserCreationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Member

class MemberCreationForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ('email','groups', 'firstname', 'lastname')


class MemberChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Member
        fields = ('email','groups', 'firstname', 'lastname', 'phone_number', 'is_active')


class NewMemberForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Member
        fields = ("email", "firstname", "lastname", "phone_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewMemberForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        member = super(NewMemberForm, self).save(commit=False)
        member.email = self.cleaned_data['email']
        member.firstname = self.cleaned_data['firstname']
        member.lastname = self.cleaned_data['lastname']
        member.phone_number = self.cleaned_data['phone_number']
        member.is_active = False
        
        if commit:
            member.save()
        return member