from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.SeePostView.as_view(), name='all_posts'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('<pk>/update_post/', views.UpdatePostView.as_view(), name='update_post'),
]