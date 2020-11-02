from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from case import views


urlpatterns = [
    path('', views.CaseList.as_view(), name='case-list'),
    path('<int:pk>', views.CaseDetail.as_view(), name='case-detail'),
    path('<int:pk>/history', views.CaseHistory.as_view(), name='case-location-history'),
]

urlpatterns = format_suffix_patterns(urlpatterns)