from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from trading.get_info import get_info, post_notification
from trading.serializers import TradingSerializer
from django.urls import reverse
import urllib


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

        return Response(get_info('/v1/getmarkets'))


class MarketView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/markets'))


class GetBoardView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/getboard'))


class BoardView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/board'))


class GetTickerView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/getticker'))


class TickerView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/ticker'))


class GetExecutionsView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/getexecutions'))


class ExecutionsView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/executions'))


class GetBoardStateView(APIView):

    def getboardstate(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/getboardstate'))


class GetHealthView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/gethealth'))


class GetChatsView(APIView):

    def get(self, request):
        """
        """
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/getchats'))

# Private API


class GetPerissionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getpermissions'))


class GetBalanceView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getbalance'))


class GetCollateralView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getcollateral'))


class GetCollateralAccountsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getcollateralaccounts'))


class GetAddressesView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getaddresses'))


class GetCoinInsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getcoinins'))


class GetCoinOutsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getcoinouts'))


class GetBankAccountsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getbankaccount'))


class GetDepositsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getdeposits'))


class GetWithdrawalsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getwithdrawals'))


class SendChildOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/sendchildorder'))


class CancelChildOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/cancelchildorder'))


class SendParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/sendparentorder'))


class CancelParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/cancelparentorder'))


class CancelAllChildOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/cancelallchildorders'))


class GetChildOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)
        path = '/v1/me/getchildorders'
        query = urllib.parse.urlencode(request.query_params)
        if query:
            path = path + '?' + query
        res = get_info(path)
        post_notification(res)
        return Response(res)


class GetParentOrdersView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)
        path = '/v1/me/getparentorders'
        query = urllib.parse.urlencode(request.query_params)
        if query:
            path = path + '?' + query
        res = get_info(path)
        post_notification(res)
        return Response(res)


class GetParentOrderView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getparentorder'))


class GetExecutionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getexecutions'))


class GetPositionsView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getpositions'))


class GetCollateralHistoryView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/getcollateralhistory'))


class GetTradingCommissionView(APIView):
    def get(self, request):
        serializer = TradingSerializer(data=request.query_params, context=request)
        serializer.is_valid(raise_exception=True)

        return Response(get_info('/v1/me/gettradingcommission'))
