from rest_framework import serializers
from home.models import to_do_bank
class Serializer_bank(serializers.ModelSerializer):
    class Meta:
        model = to_do_bank
        fields = '__all__'
