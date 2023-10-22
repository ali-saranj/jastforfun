from rest_framework.views import APIView
from rest_framework.response import Response

from salons.models import Salon
from .serializers import SearchSerializer


class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q')

        if query:
            nameSalon = Salon.objects.filter(name__icontains=query)
            serializer = SearchSerializer(nameSalon, many=True)
            return Response(serializer.data)

        return Response([])
