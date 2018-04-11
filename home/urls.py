"""News home URL Configuration.

Included directly under the root of the site.
"""

# Django imports
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

# Local imports
from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("content/<int:pk>", views.view_content, name="view_content"),
    path("profile/<int:pk>", views.view_profile, name="view_profile"),
    path("section/<path:name>", views.view_section, name="view_section")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
