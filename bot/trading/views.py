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

# Private API

class GetPerissionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getpermissions'))

class GetBalanceView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getbalance'))

class GetCollateralView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getcollateral'))

class GetCollateralAccountsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getcollateralaccounts'))

class GetAddressesView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getaddresses'))

class GetCoinInsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getcoinins'))

class GetCoinOutsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getcoinouts'))

class GetBankAccountsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getbankaccount'))

class GetDepositsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getdeposits'))

class GetWithdrawalsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getwithdrawals'))

class SendChildOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/sendchildorder'))

class CancelChildOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/cancelchildorder'))

class SendParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/sendparentorder'))

class CancelParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/cancelparentorder'))

class CancelAllChildOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/cancelallchildorders'))

class GetChildOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getchildorders'))

class GetChildOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getchildorders'))

class GetParentOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getparentorders'))

class GetParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getparentorder'))

class GetExecutionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getexecutions'))

class GetPositionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getpositions'))

class GetCollateralHistoryView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/getcollateralhistory'))

class GetTradingCommissionView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('me/gettradingcommission'))

