"""
URL configuration for workout_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.app_settings import swagger_settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.http import HttpResponseNotFound

schema_view = get_schema_view(
   openapi.Info(
      title="Workout Planner API",
      default_version='v1',
      description="API documentation for Workout Planner",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
swagger_settings.SECURITY_DEFINITIONS = {
    "Bearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
    }
}
def dummy_login(request):
    return HttpResponseNotFound("Login via JWT only.")

urlpatterns = [
    path('admin/', admin.site.urls),

    # App endpoints
    path('api/users/', include('users.urls')),
    path('api/', include('exercises.urls')),
    path('api/', include('workout_plan.urls')),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Swagger / Redoc
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Catch-all for /accounts/login/
    path('accounts/login/', dummy_login),
]
