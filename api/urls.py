from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.record_api_view_get_all.as_view()),
    path('new/', views.record_api_view_create_new.as_view()),
]
