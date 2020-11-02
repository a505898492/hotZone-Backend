from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from case import views


urlpatterns = [
    path('', views.CaseList.as_view()),
    path('detail', views.CaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)