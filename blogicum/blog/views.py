from django.shortcuts import render
from django.urls import path

from . import views
# Create your views here.


urlpatterns = [

    path('', views.index()),
    path('posts/<int:id>', views.post_detail()),
    path('category/<slug:category_slug>/', views.category_post())

]