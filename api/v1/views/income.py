from rest_framework import status, mixins, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mofisafe_app.models import Income
from api.v1.serializers import SerializeIncome
from rest_framework.views import APIView


@permission_classes([AllowAny])
class IncomeList(APIView):
    """ This class will list all incomes and create a new income
    Attributes:
        get: This will list all incomes.
        post: This will create a new income.

    Methods:
        get: This will list all incomes.
        post: This will create a new income.

    Example:
        income = IncomeList()
        income.get()
        income.post()
    """
    def get(self, request, format=None):
        """ This will list all incomes
        Args:
            request: The request object
            format: The format of the response
        Returns:
            Response: The response object
        """
        all_income = Income.objects.all()
        serializer = SerializeIncome(all_income, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """ This will create a new income
        Args:
            request: The request object
            format: The format of the response
        Returns:
            Response: The response object
        """
        object = SerializeIncome(data=request.data)
        if object.is_valid():
            object.save()
            return Response(object.data, status=status.HTTP_201_CREATED)
        return Response(object.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class IncomeDetails(APIView):
    """ This class will update, delete, or update an income
    
    Attributes:
        get: This will retrieve an income
        put: This will update an income
        delete: This will delete an income

    Example:
        income = IncomeDetails()
        income.get()
        income.put()
        income.delete()
    """

    def get(self, request, pk, format=None):
        """ This will retrieve an income
        Args:
            request: The request object
            pk: The primary key of the income
            format: The format of the response

        Returns:
            Response: The response object
        """
        try:
            object = Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        deserialized = SerializeIncome(object)
        return Response(deserialized.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        """ This will update an income
        Args:
                request: The request object
                pk: The primary key of the income
                format: The format of the response
        
        Returns:
                Response: The response object
        """
        try:
            object = Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serialized_object = SerializeIncome(object, data=request.data)
        if serialized_object.is_valid():
            serialized_object.save()
            return Response(serialized_object.data)
        return Response(serialized_object.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format):
        """ This will delete an income
        Args:
                request: The request object
                pk: The primary key of the income
                format: The format of the response
        Returns:
                Response: The response object
        """
        try:
            object = Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        object.delete()
        return Response(status=204)
