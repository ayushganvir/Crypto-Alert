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
from django.urls import include, path
import core.views

urlpatterns = [
    # path('', include(router.urls)),
    path('', core.views.api_root),
    path('users/',
         core.views.UserList.as_view(),
         name='user-list'),
    path('alert/', core.views.AlertList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

