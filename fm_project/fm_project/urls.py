"""farm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView,)  # used by jwt


# used to wire the schema url (pip install coreapi)
schema_view = get_schema_view(title='Farm Mart API', description='API endpoints for farmers', version='1.01')
swagger_view = get_swagger_view(title='FARM MART API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # this points to the users app for custom user configurations
    path('users/', include('django.contrib.auth.urls')),  # This points to django default user authentication url
    path('farms/', include('farms.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),  # used for authorization b4 accessing api views
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # used by simple jwt to obtain token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # used by simple jwt to refresh token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # used by simple jwt to verify token
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # using the inbuilt template view
    path('docs', include_docs_urls(title='Farm Mart API')),
    path('swagger-docs', swagger_view),
    path('schema', schema_view),
]
