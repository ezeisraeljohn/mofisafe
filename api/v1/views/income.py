from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from mofisafe_app.models import Income
from api.v1.serializers import SerializeIncome


class IncomeList(generics.ListCreateAPIView):

    queryset = Income.objects.all()
    serializer_class = SerializeIncome

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, args, kwargs):
        return self.create(request, args, kwargs)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Income.objects.all()
    serializer_class = SerializeIncome

    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
