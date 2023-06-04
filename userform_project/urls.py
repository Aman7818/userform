from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userform.urls')),
]
