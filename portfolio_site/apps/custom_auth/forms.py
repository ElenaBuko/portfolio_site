
from django import forms
from django.contrib.auth import authenticate

from apps.custom_auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'first_name', 'last_name', 'data_joined',
                   'is_superuser', 'is_staff', 'last_login')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(required=True, label='',
    #                            widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # password = forms.CharField(required=True, label='',
    #                            widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exits.')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect.')
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')
        return super().clean(*args, **kwargs)