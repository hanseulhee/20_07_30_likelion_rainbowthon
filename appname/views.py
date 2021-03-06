from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CustomUser
from .forms import PostForm, SigninForm, UserForm


#from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.


def main(request):
    posts = Post.objects.all()
    signin_form = SigninForm()
    return render(request, 'appname/main.html', {'posts': posts, 'signin_form': signin_form})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'appname/create.html', {'form': form})


def read(request):
    return redirect('main')


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
        return render(request, 'appname/create.html', {'form': form})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main')


def signin(request):
    if request.method == "POST":
        # 접근하는 방식이 포스트면
        username = request.POST['username']
        password = request.POST['password']
        # 우리가 만든 변수 그 값을 찾아서 이 변수에 대입한다.
        user = authenticate(username=username, password=password)
        # authenticate 값을 인증하고, 우리가 만든 user에 값을 대입함
        if user is not None:  # 유저 생성에 성공했나? 안했나에 대해 조건문으로 대입하고
            login(request, user)
            return redirect('main')
        else:  # 실패했다면 아래의 문자열을 보여줌
            return HttpResponse("로그인 실패")


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
                                                      email=form.cleaned_data['email'],
                                                      password=form.cleaned_data['password'],
                                                      nickname=form.cleaned_data['nickname'],
                                                      phone_number=form.cleaned_data['phone_number'])
            login(request, new_user)
            return redirect('main')
    else:
        form = UserForm()
        return render(request, 'appname/signup.html', {'form': form})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'appname/new.html', {'form': form})

def test(req):
    return render(req, 'main.html')
