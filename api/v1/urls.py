from django.urls import path
from income import views as incomeViews
from users import views as usersViews
from expenses import views as expenseViews
from budget import views as budgetViews
from categories import views as categoriesViews
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.views import api_root


income_list = incomeViews.IncomeViewSet.as_view({
        'get': 'list',
        'post': 'create'
})

income_details = incomeViews.IncomeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
})

expense_list = expenseViews.ExpenseViewSet.as_view({
        'get': 'list',
        'post': 'create'
})

expense_details = expenseViews.ExpenseViewSet.as_view({
        'get':'list',
        'put':'update',
        'delete': 'destroy'
})

budget_list = budgetViews.BudgetViewSet.as_view({
        'get':'list',
        'post': 'create'
})

budget_details = budgetViews.BudgetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
})

user_list = usersViews.UserViewSet.as_view({
        'get': 'list'
})

user_details = usersViews.UserViewSet.as_view({
        'get': 'retrieve'
})

categories_list = categoriesViews.CategoriesViewSet.as_view({
        'get':'list',
        'post': 'create'
})

categories_details = categoriesViews.CategoriesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
})


urlpatterns = [
        path('income/', income_list, name='income_list'),
        path('income/<int:pk>/', income_details, name='income-detail'),
        path('categories/', categories_list, name='categories_list'),
        path('categories/<int:pk>/', categories_details, name='categories-detail'),
        path('expenses/', expense_list, name='expense_list'),
        path('expense/<int:pk>/', expense_details, name='expense-detail'),
        path('budgets/', budget_list, name='budget_list'),
        path('budget/<int:pk>/', budget_details, name='budget-detail'),
        path('users/', user_list, name="users_list"),
        path('user/<int:pk>/', user_details, name="user-detail"),
        path('', api_root.api_root, name='api_root')
]

urlpatterns = format_suffix_patterns(urlpatterns)
