from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Необходимый. 150 символов или меньше. Буквы, цифры и @/./+/-/_ только.</small></span>'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['first_name'].label = ''
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Почта'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ваш пароль не должен быть слишком похож на другие ваши личные данные.</li><li>Ваш пароль должен содержать не менее 8 символов.</li><li>Ваш пароль не может быть широко используемым паролем. </li><li>Ваш пароль не может быть полностью числовым.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Введите тот же пароль, что и раньше, для проверки.</small></span>'	



# Create adding the record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ("user",)

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Номер", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Адрес", "class":"form-control"}), label="")
    dietary_needs = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Пакет", "class":"form-control"}), label="")
    #medical_condition = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"мед. требования", "class":"form-control"}), label="")  
