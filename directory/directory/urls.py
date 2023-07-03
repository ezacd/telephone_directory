from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from django.urls import re_path, include
from django.urls.converters import StringConverter
from django.urls import register_converter


class UnicodeSlugConverter(StringConverter):
    regex = '[-a-zA-Z0-9_а-яА-Я]+'


register_converter(UnicodeSlugConverter, 'slug_unicode')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('directory_app.urls')),
    path('accounts/', include('allauth.urls')),
]
