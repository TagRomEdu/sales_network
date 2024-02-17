from rest_framework import generics

from users_app.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Controller for creating user.
    """
    serializer_class = UserSerializer
