from django.urls import path
from .views import (HomeView, ArticleDetailView, AddPostView, LikeView, UpdatePostView,
                    DeletePostView, AddCatView, CategoryView, CategoryListView,
                    AddComment)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCatView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/add-comment/', AddComment.as_view(), name='add-comment')
]

