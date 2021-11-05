"""core URL Configuration."""

# Django
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView


# Graphene
from graphene_django.views import GraphQLView

# Schema
from .schema import schema




urlpatterns = [
    # Graphql Path
    path("graphql", 
        csrf_exempt(
            FileUploadGraphQLView.as_view(graphiql=True, schema=schema)
        )
    ),


    # Admin Path
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    """Enable images for debug mode."""
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

