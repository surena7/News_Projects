from django.urls import path
from django.contrib.auth import views
from accounts.views import *
from django.urls import reverse_lazy


app_name="accounts"



urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
path(
    "password_change/",
    views.PasswordChangeView.as_view(
        success_url=reverse_lazy("accounts:password_change_done")  # با namespace حساب شود
    ),
    name="password_change",
),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]




urlpatterns += [
    path("",Dashbord.as_view(),name="userpanel"),
    path("showpost/",ShowPost.as_view(),name="show"),
    path("AddPost/",Add.as_view(),name="add"),
    path("UpdatePost/<int:pk>/",Update.as_view(),name="Update"),
    path("delete/<int:pk>/",Delete.as_view(),name="Delete"),
    path("RegisterUser/",register_user,name="register"),
    path("UserProFile/",ProFile.as_view(),name="profile"),
    # path("password_change/",views.PasswordChangeView.as_view(),name="change"),

]