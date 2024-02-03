from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('generate/', views.create_post, name='create_post'),
    path('image/<int:post_id>/', views.generate_post_image, name='generate_post_image'),
]
