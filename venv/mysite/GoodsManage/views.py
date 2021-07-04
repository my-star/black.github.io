from django.shortcuts import render,redirect
from .models import User
from .forms import UserLogin,UserRegister
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self,request):
        return redirect('login/')

class LoginView(View):
    def get(self,request):
        if request.session.get('is_login', None):
            return redirect('home')
        else:
            login_form = UserLogin()
            return render(request, 'login.html', locals())
    def post(self,request):
        emp_num =request.POST['emp_num']
        password =request.POST['password']
        user = User.objects.filter(emp_num=emp_num, password=password)
        if user :
            request.session['is_login'] = True
            request.session['emp_num'] = emp_num
            # request.session['user_name'] =user.user_name
            return redirect('home')
        else:
            login_form = UserLogin()
            return render(request, 'login.html', locals())

class HomeView(View):
    def get(self,request):
        if not request.session.get('is_login',None):
            return redirect('/login/')
        else:
            return render(request, 'home.html')

class RegistView(View):
    def get(self,request):
        reg_form = UserRegister()
        return render(request, 'register.html', locals())
    def post(self,request):
        user_name = request.POST['user_name']
        emp_num = request.POST['emp_num']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.filter(emp_num=emp_num)
        if not user:
          if password2==password1:
              user = User.objects.create(user_name=user_name, emp_num=emp_num, password=password1)
              if user:
                  return redirect('/login/')
          else:
              message = 'Please input two same password'
              login_form = UserLogin()
              return render(request, 'login.html', locals())
        else:
                message = 'Please input another EmployeeNum'
                login_form = UserRegister()
                return render(reques, 'register.html', locals())
