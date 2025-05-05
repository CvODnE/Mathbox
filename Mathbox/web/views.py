from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import unquote
from django.http.response import HttpResponse
from web.models import Faq, CommmunityPost, Exercises, Games, Tools, Kids, Student
from django.urls import reverse


def index(request):
    faqs = Faq.objects.all()
    context = {
        "faqs": faqs,
    }
    return render(request, "index.html", context=context)

def doc(request):
    contents = Kids.objects.all()
    students = Student.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        contents = sorted(contents, 
                      key=lambda x: search_term in x.title.lower(), 
                      reverse=True)
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        contents = sorted(contents, 
                      key=lambda x: search_term in x.item.lower(), 
                      reverse=True)
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        students = sorted(students, 
                      key=lambda x: search_term in x.title.lower(), 
                      reverse=True)
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        students = sorted(students, 
                      key=lambda x: search_term in x.item.lower(),
                      reverse=True)
    context = {
        "contents": contents,
        "students": students,
    }
    return render(request, "doc.html", context=context)

def exercises(request):
    contents = Exercises.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        contents = sorted(contents, 
                      key=lambda x: search_term in x.about.lower(), 
                      reverse=True)
    context = {
        "contents": contents,
    }
    return render(request, "exercise.html", context=context)


def exercise(request, about_text):
    decoded_about = unquote(about_text)
    exercises = get_object_or_404(Exercises, about=decoded_about)
    return render(request, 'exercises.html', {'exercises': exercises})


def games(request):
    contents = Games.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        contents = sorted(contents, 
                      key=lambda x: search_term in x.name.lower(), 
                      reverse=True)
    context = {
        "contents": contents,
    }
    return render(request, "games.html", context=context)


def game(request, name_text):
    decoded_name = unquote(name_text)
    game = get_object_or_404(Games, name=decoded_name)
    return render(request, 'game.html', {'game': game})


def community(request):
    posts = CommmunityPost.objects.all().order_by('-created_at')
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        posts = sorted(posts, 
                      key=lambda x: search_term in x.content.lower(), 
                      reverse=True)
    context = {
        "posts" : posts
    }
    return render(request, "community.html", context=context)

def tools(request):
    contents = Tools.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search'].lower()
        contents = sorted(contents, 
                      key=lambda x: search_term in x.name.lower(), 
                      reverse=True)
    context = {
        "contents": contents,
    }
    return render(request, "tools.html", context=context)


def tool(request, name_text):
    decoded_name = unquote(name_text)
    tool = get_object_or_404(Tools, name=decoded_name)
    return render(request, 'tool.html', {'tool': tool})


def community_post(request):
    heading = request.POST.get("heading")
    image = request.FILES.get("image")
    content = request.POST.get("content")

    CommmunityPost.objects.create(
        heading = heading,
        image = image,
        content = content,
    )

    return redirect(reverse("web:community"))