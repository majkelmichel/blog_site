from django.urls import path
from . import views

urlpatterns = [
    path('', views.InfoView.as_view()),
    path('create_post/', views.get_post_data),
]