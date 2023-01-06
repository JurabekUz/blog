from re import template
from django.urls import path
from .views import ( UserRegisterView, UserEditView, PasswordsChange, 
PasswordSuccess, UserProfileView, UserEditProfile, UserCreateProfileView, DeleteProfilePage )
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/', UserEditView.as_view(), name='edit-profile'),
    path('password/',PasswordsChange.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('password_success/',PasswordSuccess, name='password_success'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name = 'user-profile'),
    path('<int:pk>/profile/edit/', UserEditProfile.as_view(), name = 'edit-user-profile'),
    path('create_profile_page/', UserCreateProfileView.as_view(), name='create_profile_page'),
    path('<int:pk>/delete_profile/', DeleteProfilePage.as_view(), name = 'delete_user_page')
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'))
    #path('password/',auth_views.PasswordChangeView.as_view())

]