from django.contrib import admin
from .models import User, Banner, Course, Category, Teacher, CustomerInfo


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'index']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'detail', 'image', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'icon_name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'detail', 'course', 'index']


class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'phone_num', 'comment']


admin.site.register(User, UserAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(CustomerInfo, CustomerInfoAdmin)
