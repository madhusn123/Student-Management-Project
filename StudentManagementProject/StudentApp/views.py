from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from StudentApp.models import City, Course, Student

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_fun(request):
    return render(request,'login.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logdata_fun(request):
    user_name = request.POST['txtname']
    user_psw = request.POST['txtpsw']
    u1 = authenticate(username=user_name,password=user_psw)# if data present in user table it will return user object or none
    if u1 is not None:

        if u1.is_superuser:
            login(request, u1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data': 'User is not a superuser'})
    else:
        return render(request, 'login.html', {'data': 'enter proper user name and password'})
    return None
# Create your views here.

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request,'register.html',{'data':  ''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    User_Name = request.POST['txtname']
    User_Email = request.POST['txtmail']
    User_Pswd = request.POST['txtpsw']

    if User.objects.filter(Q(username=User_Name) | Q(email=User_Email)).exists():
        return render(request,'register.html',{'data': 'User name and Email is already exists'})
    else:
        u1 = User.objects.create_superuser(username=User_Name,email=User_Email,password=User_Pswd)
        u1.save()
        return redirect('log')
    return None

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'City_data': city,'Course_data':course})


def read_fun(request):
    s1 = Student()
    s1.Stud_Name = request.POST['txtname']
    s1.Stud_Age = request.POST['txtage']
    s1.Stud_Phno = request.POST['txtpno']
    s1.Stud_City = City.objects.get(City_Name = request.POST['ddlCity'])
    s1.Stud_Course = Course.objects.get(Course_Name = request.POST['ddlCourse'])
    s1.save()
    return redirect('add')
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html',{'data':s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Stud_Name = request.POST['txtname']
        s1.Stud_Age = int(request.POST['txtage'])
        s1.Stud_Phno = int(request.POST['txtpno'])
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_data':city,'Course_data':course})

    return None

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out_fun(request):

    return redirect('log')