from django.urls import path
from api.v1.views import income
from api.v1.views import user
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
        path('api/v1/income/', income.IncomeList.as_view(), name='income_list'),
        path('api/v1/income/<int:pk>/', income.IncomeDetail.as_view(), name='income_details'),
        path('api/v1/users/', user.UserList.as_view(), name="users_list"),
        path('api/v1/user/<int:pk>/', user.UserDetail.as_view(), name="user_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
