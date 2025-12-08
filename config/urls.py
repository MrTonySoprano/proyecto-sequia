# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    # 👇 Home del sitio (página principal)
    path(
        "",
        TemplateView.as_view(template_name="sequia/home.html"),
        name="home",
    ),

    # Admin de Django
    path("admin/", admin.site.urls),

    # API principal
    path("api/", include("sequia.api.urls")),

    # Auth (registro/login/logout, vistas de accounts)
    path("api/auth/", include("sequia.accounts.urls")),

    # JWT “clásico”
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Documentación
    path("api/schema/", get_schema_view(title="API Sequia"), name="openapi-schema"),
    path(
        "api/docs/",
        TemplateView.as_view(
            template_name="sequia/api_redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api-docs",
    ),
]
