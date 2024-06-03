from rest_framework import status
from rest_framework.response import Response
from categories.models import Categories
from expenses.models import Expense
from income.models import Income
from budget.models import Budget
from categories.serializer import SerializeCategories
from income.serializer import SerializeIncome
from expenses.serializer import SerializeExpense
from budget.serializer import SerializeBudget


def summary(request):
        summary = {}

        income = Income.objects.filter(user=request.user)
        expense = Expense.objects.filter(user=request.user)
        budget = Budget.objects.filter(user=request.user)
        serializer_income = SerializeIncome(income, many=True)
        serializer_expense = SerializeExpense(expense, many=True)

        total_income = 0
        total_expense = 0
        for income in serializer_income.data:
                total_income += income['amount']
        summary['total_income'] = total_income

        for expense in serializer_expense.data:
                total_expense += expense['amount']
        summary['total_expense'] = total_income




