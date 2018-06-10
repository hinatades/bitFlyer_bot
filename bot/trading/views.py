from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from trading.get_info import get_info
from trading.serializers import TradingSerializer
from django.core.urlresolvers import reverse


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


class GetMarketView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getmarket'))


class MarketView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('market'))


class GetBoardView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getboard'))

class GetTickerView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getticker'))


class TickerView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('ticker'))


class GetExecutionsView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getexecutions'))


class GetBoardStateView(APIView):

    def getboardstate(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getboardstate'))


class GetHealthView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('gethealth'))


class GetChatView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getchat'))
