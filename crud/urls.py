from django.urls import path 
from .views import *

urlpatterns = [ 
    path('', article_func, name='article_func'),
    path('<slug>', article_detail, name='article_detail'),
    path('article_create/', article_create, name='article_create'),
    path('<slug>/edit', article_edit, name='article_edit'),
    path('<slug>/delete', article_delete, name='article_delete'), 
    path('<slug>/like', like_article, name='article_like'),
    path('<slug>/dislike', dislike_article, name='article_dislike'),

]