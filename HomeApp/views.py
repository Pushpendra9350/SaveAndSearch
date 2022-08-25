from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from pytz import timezone
tz = timezone('Asia/Kolkata')

def loginUser(request):
    try:
        if request.method == 'POST':
            password = request.POST['password']
            user = authenticate(request, username='admin', password=password)
            print(user, password)
            if user is not None:
                print('if')
                login(request, user)
                return redirect('home')
            else:
                print('else')
                return render(request, 'HomeApp/login.html')
        else:
            return render(request, 'error.html')
    except Exception as e:
        return render(request, 'error.html')


def loginpage(request):
    return render(request, 'HomeApp/login.html')


@login_required
def home(request):
    posts = Posts.objects.all().order_by('-last_updated')[:51]
    new_posts = []
    for i in posts:
        dicts = {} 
        dicts['id'] = str(i.pk)+'id'
        title = i.title
        dicts['title'] = title
        dicts['content'] = i.content
        new_posts.append(dicts)
    return render(request, 'HomeApp/index.html', {'posts': new_posts})


@login_required
def create(request):
    try:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            if title=='' or content=='':
                return redirect('/')
            else:
                if Posts.objects.filter(title=title).exists():
                    Posts.objects.filter(title=title).update(
                        title=title,
                        content=content,
                        last_updated = datetime.now(tz)
                    )
                else:
                    Posts.objects.create(
                        title=title,
                        content=content,
                        created_at = datetime.now(tz),
                        last_updated = datetime.now(tz)
                    )
            return redirect('/')
        else:
            return render(request, 'error.html')
    except Exception as e:
        return render(request, 'error.html')
    


@login_required
def search(request):
    try:
        if request.method == 'POST':
            search_text = request.POST['searchquery']
            posts1 = Posts.objects.filter(title__contains=search_text)
            posts2 = Posts.objects.filter(content__contains=search_text)
            new_posts = []
            counter = 0
            for i in posts1:
                counter += 1
                dicts = {}
                dicts['id'] = str(counter)+'id'
                dicts['title'] = i.title
                dicts['content'] = i.content
                new_posts.append(dicts)
            for i in posts2:
                flag = 0
                counter += 1
                dicts = {}
                dicts['id'] = str(counter)+'id'
                dicts['title'] = i.title
                dicts['content'] = i.content
                for post in new_posts:
                    if i.title in post['title']:
                        flag = 1
                        break
                if flag == 0:
                    new_posts.append(dicts)

            return render(request, 'HomeApp/index.html', {'posts': new_posts})
        else:
            return render(request, 'error.html')
    except Exception as e:
        return render(request, 'error.html')


