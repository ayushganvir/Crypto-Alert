"""alerts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core.views import UserViewSet, AlertViewSet, UserRegistrationView, UserLoginView, CurrentUser, \
    UserChangePasswordView, UserAlertView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# router = DefaultRouter()
# router.register(r'users', core.views.UserList, basename="users")

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
alert_list = AlertViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
alert_detail = AlertViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('', core.views.api_root),
    # path('register/', core.views.RegisterApi.as_view(), name='register'),
    path('current/', CurrentUser.as_view(), name='current_user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('user_alerts/', UserAlertView.as_view(), name='user_alerts'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    path('alerts/', alert_list, name='alert-list'),
    path('alerts/<int:pk>/', alert_detail, name='alert-detail'),
    path('users/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

])

