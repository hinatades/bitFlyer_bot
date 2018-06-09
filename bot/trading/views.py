from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from trading.get_info import get_info
from trading.serializers import TradingSerializer


class TradingView(APIView):

    def index(request):
        """
        """
        return render(request, 'index.html')

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info())
