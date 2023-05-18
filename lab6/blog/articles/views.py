from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                try:
                    Article.objects.get(title=form["title"])
                    form["errors"] = 'Названия статей должны быть уникальными'
                except Article.DoesNotExist:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = 'Не все поля заполнены'
            return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST['username'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        if form['username'] and form['email'] and form['password']:
            try:
                User.objects.get(username=form['username'])
                form['errors'] = 'Пользователь с таким именем уже есть.'
            except User.DoesNotExist:
                print('Этот логин свободен.')
                user = User.objects.create_user(form['username'], form['email'], form['password'])
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = 'Не все поля заполнены'
        return render(request, 'create_user.html', {'form': form})
    else:
        return render(request, 'create_user.html', {})


def login_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST['username'],
            'password': request.POST['password']
        }
        if form['username'] and form['password']:
            user = authenticate(username=form['username'], password=form['password'])
            if not user:
                form['errors'] = 'Пользователь с такими данными не зарегистрирован.'
            else:
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = 'Не все поля заполнены'
        return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('archive')

