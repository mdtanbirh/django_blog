from django.urls import path
from .import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog_about')
]
