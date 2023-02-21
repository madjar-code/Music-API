from django.contrib import admin
from django.urls import path, include, re_path
from .yasg import schema_view


API_PREFIX = 'api/v1'

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f'{API_PREFIX}/', include('music.api.urls')),
]

urlpatterns += [
   re_path(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
