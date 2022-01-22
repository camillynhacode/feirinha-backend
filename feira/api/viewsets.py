from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from feira.api.serializers import FeiraSerializer, ItemFeiraSerializer
from feira.models import Feira, ItemFeira

class FeiraviewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Feira.objects.all()
    serializer_class=FeiraSerializer

    def list(self, request):
        queryset = self.queryset.filter(usuario=request.user)
        serializer = FeiraSerializer(queryset, many=True)
        return Response(serializer.data)

class ItenFeiraviewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset=ItemFeira.objects.all()
    serializer_class=ItemFeiraSerializer

    def list(self, request):
        queryset = self.queryset.filter(feira__usuario=request.user)
        serializer = ItemFeiraSerializer(queryset, many=True)
        return Response(serializer.data)

