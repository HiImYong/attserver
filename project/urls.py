
from django.contrib import admin
from django.urls import include, path
from rest_api import urls as rest_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(rest_urls))
]
