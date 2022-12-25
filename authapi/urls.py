from django.urls import path
from authapi.views import RegisterUser, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('account/token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

