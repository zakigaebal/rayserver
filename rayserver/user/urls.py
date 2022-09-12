from django.urls import path
from .views import MobileLogin, login_view, logout_view, m_login, RegistUser, AppLogin

app_name = "user"

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout',logout_view, name='logout'), 
    
    path('regist_user', RegistUser.as_view(), name='regist_user'),
    path('app_login', AppLogin.as_view(), name='app_login'),
    
    path('m_login',MobileLogin.as_view(),name='m_login'),
]