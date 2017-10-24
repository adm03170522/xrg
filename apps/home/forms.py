from django import forms

# from .models import CustomerInfo


__author__ = 'Johnny'
__date__ = '2017/10/20 下午3:54'


# class CustomerInfoForm(forms.ModelForm):
#     class Meta:
#         model = CustomerInfo
#         fields = ['name', 'age', 'phone_num', 'comment']
class CustomerInfoForm(forms.Form):
    user_name = forms.CharField(required=True, max_length=2,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': '学员姓名'}))
    age = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': '学员年龄'}))
    phone_num = forms.CharField(required=True, max_length=11,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': '联系电话'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '预约试听课程...比如：绘画课'
    }))
