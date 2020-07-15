from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage,name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("pub_entry/", views.pub_entry, name="pub_entry"),
    path("add_entry/", views.add_entry, name="add_entry"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path("thisweek/", views.thisweek, name="thisweek"),
    path("allentry/", views.allentry, name="allentry"),
    path("Search/", views.Search, name="Search"),
    
]
