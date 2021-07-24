from django.urls import path
from .views import CategoryListView, HomeView,article_view,AddPost,EditPost,DeletePost,CategoryView,AddCategory,CategoryListView,LikeView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',article_view.as_view(),name='article'),
    path('addpost/',AddPost.as_view(),name="addpost"),
    path('editpost/<int:pk>',EditPost.as_view(),name="editpost"),
    path('deletepost/<int:pk>',DeletePost.as_view(),name="deletepost"),
    path('addcategory/',AddCategory.as_view(),name="addcategory"),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='categorylist'),
    path('like/<int:pk>',LikeView,name="like_post"),
]