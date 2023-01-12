from rest_framework.urls import  path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from users.views import SignUp
from users.views import SignIn


urlpatterns = [
    path('api/v1/regis/', SignUp.as_view({"post":"create"})),
    path('api/v1/login/', SignIn.as_view(), name='jwt_create'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),
]
