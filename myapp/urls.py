
from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('homepage/',views.admin_home),
    path('add_police/',views.admin_add_police),
    path('add_police_post/',views.admin_add_police_post),
    path('changepassword/',views.admin_change_password),
    path('changepassword_post/',views.admin_change_password_post),
    path('complaints/',views.admin_complaints),
    path('complaints_post/',views.admin_complaints_post),
    path('edit_police/',views.admin_edit_police),
    path('edit_police_post/',views.admin_edit_police_post),
    path('suspicious_activity/',views.admin_suspicious_activity),
    path('suspicious_activity_post/',views.admin_suspicious_activity_post),
    path('app_reviews/',views.admin_view_appreviews),
    path('app_reviews_post/',views.admin_view_appreviews_post),
    path('view_criminals/',views.admin_view_criminals),
    path('view_criminals_post/',views.admin_view_criminals_post),
    path('view_police/', views.admin_view_police),
    path('view_police_post/', views.admin_view_police_post),
    path('registered_users/',views.admin_view_registered_users),
    path('registered_users_post/',views.admin_view_registered_users_post),
    #users
    path('add family member/',views.user_add_family_members),
    path('chat/',views.user_chat),
    path('review/',views.user_review),
    path('view and edit profile/',views.user_view_and_edit_profile),
    path('view criminals/',views.user_view_criminals),
    path('family members/',views.user_view_family_members),
    #police
    path('add criminals/',views.police_add_criminals),
    path('police view criminals/',views.police_view_criminals),
]
