from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """ Get the root api"""
    return Response({
        'users': reverse('users_list', request=request, format=format),
        'incomes': reverse('income_list', request=request, format=format)
    })
