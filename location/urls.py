from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from location import views


urlpatterns = [
    path('locations', views.LocationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)