"""adv_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from View import main_views as view
from View import users_views as u_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls'), name = "posts"),
    path('', view.index, name = "index"),
    path('equipe/', view.team, name = "team"),
    path('somenteadvogados/cadastro-admin/', u_view.register, name = 'register'),
    path('somenteadvogados/login-admin/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('#', auth_views.LogoutView.as_view(template_name='index.html'), name = 'logout'),
]
