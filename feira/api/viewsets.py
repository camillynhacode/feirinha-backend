from rest_framework.viewsets import ModelViewSet
from feira.api.serializers import FeiraSerializer, ItemFeiraSerializer

from feira.models import Feira, ItemFeira

class FeiraviewSet(ModelViewSet):
    queryset=Feira.objects.all()
    serializer_class=FeiraSerializer

class ItenFeiraviewSet(ModelViewSet):
    queryset=ItemFeira.objects.all()
    serializer_class=ItemFeiraSerializer

