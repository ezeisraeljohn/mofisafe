from django.urls import path
from api.v1.views import income
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
        path('api/v1/income/', income.IncomeList.as_view(), name='income_list'),
        path('api/v1/income/<int:pk>/', income.IncomeDetails.as_view(), name='income_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)