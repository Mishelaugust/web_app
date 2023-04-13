from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('record/<int:pk>', views.manager_record, name = 'record'),
    path('delete/<int:pk>', views.manager_delete_record, name = 'delete'),
    path('add/', views.manager_add_record, name = 'add'),
]
