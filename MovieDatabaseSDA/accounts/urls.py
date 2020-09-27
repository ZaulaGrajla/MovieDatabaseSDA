from django.urls import path

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeView, SuccessMessagedLogoutView

app_name = 'accounts'

urlpatterns = [
    path("login/", SubmittableLoginView.as_view(), name='login'),
    path("editpass/", SubmittablePasswordChangeView.as_view(), name='edit_pass'),
    path("logout/", SuccessMessagedLogoutView.as_view(), name='logout'),
]
