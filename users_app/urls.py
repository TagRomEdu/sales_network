from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
    )

from users_app.apps import UsersAppConfig
from users_app.api_views import UserCreateAPIView

app_name = UsersAppConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
]
