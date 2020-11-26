"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='blog-home'),
    path('article/<int:pk>', Article.as_view(), name='article-page'), # primary key
    path('add_post', AddPost.as_view(), name='add-post'),
    path('article/edit/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePost.as_view(), name='delete-post')
]
