from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # REGISTER & lOGIN URL PATHS
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    # USER-PRODUCT ACCESS URL PATHS
    path('product/', views.products, name='products'),
    path('CreateProduct/', views.CreateProduct, name='CreateProduct'),
    path('UpdateProduct/<str:pk>/', views.UpdateProduct, name='UpdateProduct'),


    # PASSWORD RESET URL PATHS
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="backend/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="backend/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="backend/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="backend/password_reset_done.html"), name="password_reset_complete"),

]