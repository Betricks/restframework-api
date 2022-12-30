from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
	path('', views.PostList.as_view(), name='home'),
    path('users/', views.UserListView.as_view()),
    path('user/<slug:pk>/', views.UserDetailView.as_view()),
    path('userdel/<slug:pk>/', views.UserDeleteView.as_view()),
    path('change-password/', views.PasswordChangeAPIVew.as_view()),
    path('register/', views.MycustomUserView.as_view(), name='register'),
	 path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
