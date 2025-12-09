# config/urls.py
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer
from django.views.generic import TemplateView

# Vista de esquema SOLO en JSON (no usa YAML, así evitamos pyyaml)
schema_view = get_schema_view(
    title="API Sequia",
    description="Esquema OpenAPI de la API Sequia",
    version="1.0.0",
    public=True,
    renderer_classes=[JSONOpenAPIRenderer],
)

urlpatterns = [
    # Home HTML
    path(
        "",
        TemplateView.as_view(template_name="sequia/home.html"),
        name="home",
    ),

    # Admin de Django
    path("admin/", admin.site.urls),

    # API principal (tus endpoints)
    path("api/", include("sequia.api.urls")),

    # Auth (login/registro/logout por vistas)
    path("api/auth/", include("sequia.accounts.urls")),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Esquema OpenAPI (solo JSON)
    path("api/schema/", schema_view, name="openapi-schema"),

    # ReDoc (documentación usando el esquema de arriba)
    path(
        "api/docs/",
        TemplateView.as_view(
            template_name="sequia/api_redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api-docs",
    ),
]
