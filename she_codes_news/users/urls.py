from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='userProfile'),
    path('profile/<str:slug>/', views.UserProfileView.as_view(), name='userProfile'),
    # path('profile/update-account/', views.UpdateAccountView.as_view(), name='updateAccount')
]