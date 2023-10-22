from rest_framework import serializers

from salons.models import Salon

from persons.serializers import PersonSerializer

from images.serializers import ImageSerializer


class SearchSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    person = PersonSerializer(read_only=True, many=True)
    class Meta:
        model = Salon
        fields = '__all__'
