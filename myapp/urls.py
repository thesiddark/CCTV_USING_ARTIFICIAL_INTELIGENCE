
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
    path('admin_complaints_post/',views.admin_complaints_post),
    path('edit_police/<id>',views.admin_edit_police),
    path('edit_police_post/',views.admin_edit_police_post),
    path('suspicious_activity/',views.admin_suspicious_activity),
    path('admin_suspicious_activity_post/',views.admin_suspicious_activity_post),
    path('app_reviews/',views.admin_view_appreviews),
    path('admin_view_appreviews_post/',views.admin_view_appreviews_post),
    path('view_criminals/',views.admin_view_criminals),
    path('view_criminals_post/',views.admin_view_criminals_post),
    path('view_police/', views.admin_view_police),
    path('admin_view_police_post/', views.admin_view_police_post),
    path('admin_delete_police/<id>',views.admin_delete_police),
    path('registered_users/',views.admin_view_registered_users),
    path('registered_users_post/',views.admin_view_registered_users_post),
    path('send_reply_post/',views.send_reply_post),
    path('send_reply/<id>',views.send_reply),
    #users
    # path('user_add_family_members/',views.user_add_family_members),
    # path('chat/',views.user_chat),
    # path('review/',views.user_review),
    # path('view and edit profile/',views.user_view_and_edit_profile),
    path('view criminals/',views.user_view_criminals),
    path('family members/',views.user_view_family_members),
    #police
    path('police_add_criminals/',views.police_add_criminals),
    path('police_add_criminals_post/',views.police_add_criminals_post),
    path('police_view_criminals/',views.police_view_criminals),
    path('police_view_criminals_post/',views.police_view_criminals_post),
    path('police_change_password/',views.police_change_password),
    path('police_change_password_post/',views.police_change_password_post),
    path('police_view_profile/',views.police_view_profile),
    path('police_add_suspicious_activity/',views.police_add_suspicious_activity),
    path('police_add_suspicious_activity_post/',views.police_add_suspicious_activity_post),
    path('policehome/',views.policehome),
    path('police_suspicious_activity/',views.police_suspicious_activity),
    path('police_suspicious_activity_post/',views.police_suspicious_activity_post),
    path('police_view_registered_users_post/',views.police_view_registered_users_post),
    path('police_view_registered_users/',views.police_view_registered_users),
    path('police_edit_criminals_post/',views.police_edit_criminals_post),
    path('police_edit_criminals/<id>',views.police_edit_criminals),
    path('police_delete_criminal/<id>',views.police_delete_criminal),
    path('police_edit_suspicious_activity/<id>',views.police_edit_suspicious_activity),
    path('police_edit_suspicious_activity_post/',views.police_edit_suspicious_activity_post),
    path('p_view_detect_det/',views.p_view_detect_det),
    path('p_search_view_detect_det/',views.p_search_view_detect_det),
    path('view_detect_det/',views.view_detect_det),
    path('search_view_detect_det/',views.search_view_detect_det),




    path('chat/<id>', views.chat1),
    path('chat_view/', views.chat_view),
    path('chat_send/<msg>', views.chat_send),

    path('user_sendchat/', views.User_sendchat),
    path('user_viewchat/', views.User_viewchat),






    #user

    path('userlogin/', views.userlogin),
    path('user_signup/', views.user_signup),
    path('and_changepassword/', views.and_changepassword),
    path('and_viewprofile/', views.and_viewprofile),
    path('user_edit_profile/', views.user_edit_profile),
    path('user_view_family_members/', views.user_view_family_members),
    path('user_add_family_members_post/', views.user_add_family_members_post),
    path('user_edit_family_members_post/', views.user_edit_family_members_post),
    path('delete_family_person/', views.delete_family_person),
    path('send_complaints/', views.send_complaints),
    path('view_user_reply/', views.view_user_reply),
    path('send_review/', views.send_review),
    path('user_view_criminals/', views.user_view_criminals),
    path('user_view_policestation/', views.user_view_policestation),
    path('user_view_suspicious/', views.user_view_suspicious),
    path('forward_suspicious_activity_post/', views.forward_suspicious_activity_post),
    path('View_Detected_Criminal/', views.View_Detected_Criminal),
    path('View_Detected_Criminal_search/', views.View_Detected_Criminal_search),


    path('logout/', views.logout),

]
