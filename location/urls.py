from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from location import views


urlpatterns = [
    path('', views.LocationList.as_view()),
    path('search', views.SearchList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)