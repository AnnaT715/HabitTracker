from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_habits),
    path('createhabit', views.create_habit),
    path('updatehabit', views.update_habit)
]