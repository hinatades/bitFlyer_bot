from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from trading.get_info import get_info
from trading.serializers import TradingSerializer
from django.urls import reverse


class TradingView(APIView):

    def get(self, request):
        """
        """

        return render(request, 'index.html')


class GetMarketView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getmarkets'))


class MarketView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('markets'))


class GetBoardView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getboard'))


class BoardView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('board'))


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

class ExecutionsView(APIView):
    
    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('executions'))
    

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


class GetChatsView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('getchats'))
