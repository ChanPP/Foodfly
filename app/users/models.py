from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

__all__ = (
    'SignupForm',
)


class SignupForm(forms.Form):
    username = forms.CharField(label='아이디')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    telephone = forms.CharField(label="연락처", max_length=11)
    address = forms.CharField(label='배송지')
    signup_hub = forms.CharField(label='가입경로 Test')
    Terms_conditions = forms.CharField(label='이용약관 test')

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError('이미 사용중인 아이디입니다')
        return data

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('비밀번호와 비밀번호 확인란의 값이 다릅니다')
        return password2

#test