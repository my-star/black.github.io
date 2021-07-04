from django import forms

class UserLogin(forms.Form):
    emp_num = forms.CharField(label='EmployeeNum')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class UserRegister(forms.Form):
    user_name = forms.CharField(label='Username',max_length=20)
    emp_num = forms.CharField(label='EmployeeNum',min_length=6,max_length=6)
    password1 = forms.CharField(label='EnterPassword',min_length=8)
    password2 = forms.CharField(label='ConfirmPassword',min_length=8)
