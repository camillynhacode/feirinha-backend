from dataclasses import fields
from feira.models import Feira, ItemFeira
from rest_framework.serializers import ModelSerializer

class FeiraSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Feira 

    
class ItemFeiraSerializer (ModelSerializer):
    class Meta:
        fields='__all__'
        model=ItemFeira
        