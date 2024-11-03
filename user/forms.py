from django import forms
from django.contrib.auth.forms import AuthenticationForm # из коробки
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class UserLoginForm(AuthenticationForm):



    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


# class UserRegistrationForm(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField()
#     password2 = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = (
#
#             "username",
#             "password1",
#             "password2",
#         )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']



class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "username",)

    image = forms.ImageField(required=False)
    username = forms.CharField()

