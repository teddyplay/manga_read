from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import RegisUserSerializer
from rest_framework import viewsets

class SignUp(viewsets.ModelViewSet):
    """API endpoint for registering a new user."""
    serializer_class = RegisUserSerializer

    def create(self, request):
        """
        The `post` method is used to create a new user instance using the provided
        user data.
        """
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Пользователь успешно зарегестрирован!",
                "data": {"username" :serializer.data.get("username"),
                         "nickname":serializer.data.get("nickname")}
            }
            return Response(data=response)
        return Response(data=serializer.errors)


class SignIn(APIView):
    """API endpoint for signing in and checking the status of a user's session."""

    def post(self, request: Request):
        """
        "post" for signing in a user using their email and password
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken().for_user(user)
            response = {
                "Сообщение": "Вы успешно вошли в систему!",
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                "user": user.username
            }
            return Response(data=response)
        else:
            return Response(data={"Сообщение": "Вы не аторизованы! \nЗарегестрируйтесь!"})

    def get(self, request: Request):
        """
        "get" for checking the status of a user's session
        """
        context = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(data=context)
