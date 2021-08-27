from django.contrib import admin
from django.urls import path, include

# imports de documentacion
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# documentacion swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Documentacion de la api del blog de Kevin",
        terms_of_service="",
        contact=openapi.Contact(email="ikevin1992@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls documentacion swagger
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),
    # auth/users
    path('api/', include('users.api.router'))
]