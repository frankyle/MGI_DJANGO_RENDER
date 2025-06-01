from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TradingIndicators
from .serializers import TradingIndicatorsSerializer
from rest_framework.permissions import IsAuthenticated

class TradingIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = TradingIndicators.objects.all()
    serializer_class = TradingIndicatorsSerializer
    permission_classes = [IsAuthenticated] 

    def create(self, request):
        request.data['trade_detail'] = request.data.get('trade_detail')  # Assuming you provide the trade_detail ID

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
