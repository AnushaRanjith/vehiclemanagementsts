"""
URL configuration for vehicleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vehiapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='Home_view'),
    path('userlogin',views.UserView.as_view(),name='userlogin_view'),

    path('reg',views.UserRegisterView.as_view(),name='reg_view'),

    path('log',views.UserLoginView.as_view(),name='Login_view'),
    path('logout',views.LogoutView.as_view(),name='Logout_view'),
    path('create',views.VehicleCreateView.as_view(),name='create_view'),
    path('list',views.VehicleListView.as_view(),name='list_view'),
    path('edit/<int:id>',views.EditView.as_view(),name='edit_view'),
    path('delete/<int:id>',views.DeleteView.as_view(),name='delete_view'),
    path('user/profile',views.UserprofileView.as_view(),name='userprofile_view'),

    
]
