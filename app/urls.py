from django.conf.urls import url
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^import/$', views.import_library)
]

urlpatterns = format_suffix_patterns(urlpatterns)
