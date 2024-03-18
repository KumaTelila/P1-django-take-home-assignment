from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckSerializer

class FoodTruckListAPIView(APIView):
    def get(self, request):
        trucks = FoodTruck.objects.all()
        serializer = FoodTruckSerializer(trucks, many=True)
        return Response(serializer.data)
