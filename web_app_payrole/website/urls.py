from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('record/<int:pk>', views.manager_record, name = 'record'),
    path('delete/<int:pk>', views.manager_delete_record, name = 'delete'),
    path('add/', views.manager_add_record, name = 'add'),
    path('update/<int:pk>', views.update_manager_record, name = 'update'),
    path('profile/', )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)