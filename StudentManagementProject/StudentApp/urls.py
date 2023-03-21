from django.urls import path
from StudentApp import views
urlpatterns = [
    path('',views.log_fun,name='log'),# login file
    path('logdata',views.logdata_fun),#it will read the data and verify
    path('reg',views.reg_fun,name='reg'), # registration file
    path('regdata',views.regdata_fun),# to read data
    path('home',views.home_fun,name='home'),
    path('add_student',views.addstudent_fun,name='add'),
    path('readdata',views.read_fun),# it will add student to table
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun, name='update'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log')

]