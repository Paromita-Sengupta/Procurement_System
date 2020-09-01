from rest_framework.generics import ListAPIView, RetrieveAPIView

from procurement.models import Component
from procurement.serializers import ComponentSerializer


class ComponentAPIList(ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentAPIRetrieve(RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
