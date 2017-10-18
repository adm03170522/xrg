from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def course(request):
    return render(request, 'home/course.html')


def teacher(request):
    return render(request, 'home/teacher.html')


def contact(request):
    return render(request, 'home/contact.html')
