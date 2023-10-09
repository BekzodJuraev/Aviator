from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#app_name='aviator2'

urlpatterns=[
     path('', views.login_page, name='login'),
     path('register/', views.register_page, name='register'),
     path('aviator/',views.AviatorView.as_view(),name="logging"),
     path('password-reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]