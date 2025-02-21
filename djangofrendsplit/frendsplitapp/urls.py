from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('learn-more/', views.learn_more, name='learn_more'),
    path('logout/', views.logout, name='logout'),
]