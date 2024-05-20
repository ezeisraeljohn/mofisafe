from django.urls import path
from api.v1.views import income
from api.v1.views import user
from api.v1.views import expense
from api.v1.views import budget
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.views import api_root


income_list = income.IncomeViewSet.as_view({
        'get': 'list',
        'post': 'create'
})

income_details = income.IncomeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
})

expense_list = expense.ExpenseViewSet.as_view({
        'get': 'list',
        'post': 'create'
})

expense_details = expense.ExpenseViewSet.as_view({
        'get':'list',
        'put':'update',
        'delete': 'destroy'
})

budget_list = budget.BudgetViewSet.as_view({
        'get':'list',
        'post': 'create'
})

budget_details = budget.BudgetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
})

user_list = user.UserViewSet.as_view({
        'get': 'list'
})

user_details = user.UserViewSet.as_view({
        'get': 'retrieve'
})

urlpatterns = [
        path('income/', income_list, name='income_list'),
        path('income/<int:pk>/', income_details, name='income-detail'),
        path('expenses/', expense_list, name='expense-list'),
        path('expense/<int:pk>/', expense_details, name='expense-detail'),
        path('budgets/', budget_list, name='budget_list'),
        path('budget/<int:pk>/', budget_details, name='budget-detail'),
        path('users/', user_list, name="users_list"),
        path('user/<int:pk>/', user_details, name="user-detail"),
        path('', api_root.api_root, name='api_root')
]

urlpatterns = format_suffix_patterns(urlpatterns)
