"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from hansimes.views import home
from hansimes.views import about
from hansimes.views import contact
from hansimes.views import service
from hansimes.views import login
from hansimes.views import register
from hansimes.views import logout_view
from hansimes.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeScreen/', home, name='homeScreen'),
    path('contact/', home, name='contact_us'),#homeform
    path('aboutPage/', about, name='aboutPage'),
    path('contactPage/', contact, name='contactPage'),
    path('contact/', contact, name='contact'),#form
    path('servicePage/', service, name='servicePage'),
    path('loginPage/', login, name='loginPage'),
    path('login/', login, name='login'),#form
    path('registerPage/', register, name='registrationPage'),
    path('register/', register, name='register'),#form
    path('logoutPage/', logout_view, name='logoutPage'),
    path('dashboardPage/', dashboard, name='dashboardPage')
]
