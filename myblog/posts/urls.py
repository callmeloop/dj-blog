from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('all_posts/', views.SeePostView.as_view(), name='see_posts'),
    path('<pk>/update_post/', views.UpdatePostView.as_view(), name='update_post'),
]