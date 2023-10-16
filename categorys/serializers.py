from rest_framework import serializers

from .models import Category
from salons.models import Salon
from salons.serializers import SalonSerializer


class CategorySerializer(serializers.ModelSerializer):
    salon = SalonSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'




