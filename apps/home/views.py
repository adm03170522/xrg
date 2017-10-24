from django.shortcuts import render, redirect, reverse
from .models import Banner, Category, Course, Teacher
from .forms import CustomerInfoForm
from .models import CustomerInfo
from xrg import settings


# Create your views here.
def index(request):
    all_banners = Banner.objects.all()
    all_categories = Category.objects.all()
    all_courses = Course.objects.all()
    return render(request, 'home/index.html', {
        'all_banners': all_banners,
        'all_categories': all_categories,
        'all_courses': all_courses
    })


def course(request):
    all_courses = Course.objects.all()
    # inner_banners = Banner.objects.filter(index='100')[:3]
    return render(request, 'home/course.html', {
        'all_courses': all_courses,

    })


def teacher(request):
    all_teachers = Teacher.objects.all()
    return render(request, 'home/teacher.html', {
        'all_teachers': all_teachers
    })


def contact(request):
    if request.method == 'POST':
        customer_info_form = CustomerInfoForm(request.POST)
        if customer_info_form.is_valid():
            user_name = request.POST.get('user_name', '')
            age = request.POST.get('age', '')
            phone_num = request.POST.get('phone_num', '')
            message = request.POST.get('message', '')
            customer_info = CustomerInfo(name=user_name, age=age,
                                         phone_num=phone_num, comment=message)
            customer_info.save()
            return redirect(reverse('home:contact'))
        else:
            return render(request, 'home/contact.html', {
                'customer_info_form': customer_info_form,
                'settings': settings
            })
    if request.method == 'GET':
        customer_info_form = CustomerInfoForm()
        return render(request, 'home/contact.html', {
            'customer_info_form': customer_info_form,
            'settings': settings
        })
