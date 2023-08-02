from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('courses/', views.courses, name='courses'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit-profile', views.editProfile, name='edit'),
    path('logout/', views.logoutUser, name="logout")



]