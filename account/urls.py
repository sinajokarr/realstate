from django.urls import path
from .views import SignUpView, UserUpdateViews, ProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/edit/", UserUpdateViews.as_view(), name="profile_edit"),
    path("profile/", ProfileView.as_view(), name="profile"),
]