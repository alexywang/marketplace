from django.urls import path 
import user.views
from django.contrib.auth.views import *

urlpatterns = [path('register',user.views.register,name='register'), 
               path('', user.views.index ,name='index'),
               path('login',user.views.do_login,name='login'),
               path('logout',user.views.do_logout,name='logout'),
               path('activate/<uidb64>/<token>/', user.views.activate, name='activate'),
               path('profile', user.views.get_user, name='profile'),
                path('password_reset', PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
                path('password_reset/done', PasswordResetDoneView.as_view(template_name='user/password_reset_landing.html'), name='password_reset_done'),
                path('reset/<uidb64>/<token>',
                    PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
                path('reset/done', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
               ]