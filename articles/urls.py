from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    createComment,
    createpcomment,
    
    )
urlpatterns =[
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>',ArticleDetailView.as_view(), name='article_detail'),
    path('new/',ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/create/<int:article_id>', createComment, name="create_comment"),
    path('comment/pcreate/<int:comment_id>', createpcomment, name="pcreate_comment")

]