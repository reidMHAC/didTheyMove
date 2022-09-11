from django.urls import path, re_path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('didTheyMove/', views.DidTheyMoveView.as_view({'get': 'list'}), name="didTheyMove"),
    path('uploadClients/', views.ClientlistView.as_view({'get': 'list'}), name="uploadClients"),
    re_path('checkMoved/(?P<client_name>\D+)/', views.CheckMovedView.as_view(), name="checkMoved"),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', views.getRoutes),
    path('test/', views.testEndPoint, name='test')
]