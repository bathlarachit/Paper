"""eper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eapp import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('createExam/',views.Category.as_view(),name='exam'),
    path('login/',auth_view.LoginView.as_view(template_name='eapp/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('list/',views.Catlist.as_view(),name='list'),
    path('exam/<int:id>/',views.examlist,name='exam'),
    path('createexam/<int:id>/',views.Exam.as_view(),name='create_exam'),
    path('qlist/<int:pk>/',views.question,name='qlist'),
    path('tfq/<int:pk>/',views.TFV.as_view(),name='tfq'),
    path('dis/<int:pk>/',views.DisV.as_view(),name='dis'),
    path('fill/<int:pk>/',views.fillV.as_view(),name='fill'),
    path('courses/',views.CourseEnroll.as_view(),name='enroll'),
    path('req/',views.Requests.as_view(),name='req'),
    path('det/<int:pk>/',views.Detail.as_view(),name='det'),
    path('del/<int:pk>/',views.ReqDelete.as_view(),name='del'),
]
