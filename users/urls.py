from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserListAPIView, UserDeleteAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserCreateAPIView.as_view(), name='login_user'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='detail_user'),
    path('delete/', UserDeleteAPIView.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
