from django.urls import path, include
from rest_framework import routers
from pets import views
from .import views
from .views import RegistrationView
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('pets/', views.PetsApiList.as_view(), name='pets'),
    path('pets/<int:pk>/', views.PetsDetailApi.as_view(), name='pets_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]

