from django import forms
from .models import Post, CustomUser
#from django.contrib.auth.models import User
#어스에서 제공하는 유저 모델을 가져오겠다.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

#모델 폼으로 입력 받은것과 같은것으로 모델은 유저, 받을 것은 비밀번호랑 패스워드 
class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','nickname', 'phone_number']