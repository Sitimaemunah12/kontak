from django.contrib import admin
from django.urls import path
from . import views
from .views import  datasiswa, dataperusahaan
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sigup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('index/', views.index, name= 'index'),
    path('index/sekolah/', views.data, name= 'sekolah'),
    path('index/siswa/', datasiswa),
    path('index/perusahaan/', dataperusahaan),

    

]
