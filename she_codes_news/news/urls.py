from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/update', views.UpdateStoryView.as_view(), name='updateStory'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/delete/', views.DeleteStory.as_view(), name='deleteStory'),
    path('author/<str:slug>/', views.ViewUsersStories.as_view(), name='usersStories')
]
