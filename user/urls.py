from django.urls import path 
import user.views

urlpatterns = [path('register',user.views.register,name='register'), 
               path('', user.views.index,name='index'),
               path('login',user.views.do_login,name='login'),
               path('logout',user.views.do_logout,name='logout'),
               ]