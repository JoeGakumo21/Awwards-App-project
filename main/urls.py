from django.urls import path
from .import views

app_name="main"

urlpatterns = [
    path('',views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addproject/',views.add_project , name="add_project"),
]