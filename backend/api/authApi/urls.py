from django.urls import path
from .views import RegisterUserView,LoginUserView,CustomPasswordResetView,customResetPasswordDone,customPasswordResetConfirm,customPasswordResetCompleteView,ProfileView,RefreshTokenView
urlpatterns = [
    path("register/",RegisterUserView.as_view(),name="register"),
    path("login/",LoginUserView.as_view(),name="login"),
    path('password_reset/',CustomPasswordResetView.as_view(),name="reset_password"),
    path("reset/<uidb64>/<token>/",customPasswordResetConfirm.as_view(),name="password_reset_confirm"),
    path('password_reset_done/',customResetPasswordDone.as_view(),name="password_reset_done"),
    path("reset_done/",customPasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='get_update_profile'),
    path("refreshToken/<int:user_id>/",RefreshTokenView.as_view(),name="refresh_token")
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    #path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
]