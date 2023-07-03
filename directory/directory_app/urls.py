from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('organization/<int:pk>', Organizations.as_view(), name='organization'),
    path('department/', Department.as_view(), name='department'),
    path('search/', search, name='search'),
    path('search_official/', search_official, name='search_official'),
    path('management/', management, name='management'),
    path('update/<int:pk>', UpdateWorker.as_view(), name='update'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
    path('import_from_excel/', import_from_excel, name='import_from_excel')
]