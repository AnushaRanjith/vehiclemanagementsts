from django.shortcuts import render,redirect

# Create your views here.
from django.db.models.query import QuerySet

from django.views import View
from django.http import HttpResponse
from vehiapp.forms import UserRegisterForm,UserLoginForm,VehicleCreateForm,EditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from vehiapp.models import VehiModel
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'register.html',{'form':form})  
    def post(self,request):
        data=UserRegisterForm(request.POST)
        if data.is_valid():
            formdata=data.cleaned_data
            User.objects.create_user(**formdata)
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid credentials")

class Home(TemplateView):
    template_name='home.html'

class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})  
    def post(self,request):
        cusname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=cusname,password=psw)
        if user:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('userlogin_view')
        else:
            messages.error(request,'invalid credentials')
            return redirect('Home_view')

class LogoutView(View) :
    def get(self,request):
        return redirect('Home_view')
    
class VehicleCreateView(CreateView):
    form_class=VehicleCreateForm
    template_name='create.html'
    model=VehiModel
    context_object_name="formdata"
    success_url=reverse_lazy('Home_view')

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"complaint created successfully")
        return super().form_valid(form)
    
class VehicleListView(ListView):
    model=VehiModel
    template_name='vehiclelist.html'
    context_object_name="data"
    def get_queryset(self) :
        return VehiModel.objects.filter(user=self.request.user)
    
class EditView(UpdateView):
    model=VehiModel
    form_class=EditForm
    template_name='edit.html'
    success_url=reverse_lazy('list_view')
    pk_url_kwarg='id'

class DeleteView(DeleteView):
    model=VehiModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('list_view')
    template_name='delete.html'

class UserView(View) :
    def get(self,request):
        return render(request,'userlogin.html')
    
class UserprofileView(View):
    def get(self,request):
        user=User.objects.filter(username=request.user)
        return render(request,'user_profile.html',{'data':user})


 



