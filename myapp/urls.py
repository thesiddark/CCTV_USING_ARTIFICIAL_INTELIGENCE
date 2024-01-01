
from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('add police/',views.admin_add_police),
    path('change password/',views.admin_change_password),
    path('complaints/',views.admin_complaints),
    path('edit police/',views.admin_edit_police),
    path('suspicious_activity/',views.admin_suspicious_activity),
    path('app reviews/',views.admin_view_appreviews),
    path('view criminals/',views.admin_view_criminals),
    path('view police/', views.admin_view_police),
    path('register users/',views.admin_view_registered_users)
]
