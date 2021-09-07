from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):   
     
     class Meta:
        model=MyUser
        fields=('email', 'username', 'phone', 'password1', 'password2')

class UserLoginForm(forms.ModelForm):
    email_or_phone = forms.CharField()
    password=forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model=MyUser
        fields=('email_or_phone', 'password')

    def clean(self):
        if self.is_valid():
            # Takes Email or phone Number
            email_or_phone=self.cleaned_data['email_or_phone']
            password=self.cleaned_data['password']
            if not authenticate(email_or_phone=email_or_phone,password=password):
                raise forms.ValidationError('invalid credential')


