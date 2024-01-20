from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from refferals.forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registeration', views.registration, name='registration'),
    path('', views.tenantRegistration , name='register'),
    path('customer_invoice/<int:id>/', views.editInvoice, name='edit_invoice'),
    path('customer_invoice/', views.customerInvoice, name='customer_invoice'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name ='login'),
    
    #passoword reset urls    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]