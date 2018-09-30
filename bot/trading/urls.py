from django.urls import path, include
from . import views

 
urlpatterns = [
    # Public API
    path('', views.TradingView.as_view(), name='index'),
    path('getmarkets', views.GetMarketView.as_view(), name='getmarkets'),
    path('markets', views.MarketView.as_view(), name='markets'),
    path('getboard', views.GetBoardView.as_view(), name='getboard'),
    path('board', views.GetBoardView.as_view(), name='board'),
    path('getticker', views.GetTickerView.as_view(), name='getticker'),
    path('ticker', views.TickerView.as_view(), name='ticker'),
    path('getexecutions', views.GetExecutionsView.as_view(), name='getexecutions'),
    path('executions', views.ExecutionsView.as_view(), name='executions'),
    path('getboardstate', views.GetBoardStateView.as_view(), name='getboardstate'),
    path('gethealth', views.GetHealthView.as_view(), name='gethealth'),
    path('getchats', views.GetChatsView.as_view(), name='getchats'),
    # Private API
    path('me/getpermissions', views.GetPerissionsView.as_view(), name='ticker'),
    path('me/getbalance', views.GetBalanceView.as_view(), name='getexecutions'),
    path('me/getcollateral', views.GetCollateralView.as_view(), name='executions'),
    path('me/getcollateralaccounts', views.GetCollateralAccountsView.as_view(), name='getboardstate'),
    path('me/getaddresses', views.GetAddressesView.as_view(), name='gethealth'),
    path('me/getcoinins', views.GetCoinInsView.as_view(), name='getchats'),
    path('me/getcoinouts', views.GetCoinOutsView.as_view(), name='executions'),
    path('me/getbankaccounts', views.GetBankAccountsView.as_view(), name='getboardstate'),
    path('me/getdeposits', views.GetDepositsView.as_view(), name='gethealth'),
    path('me/getwithdrawals', views.GetWithdrawalsView.as_view(), name='getchats'),
    path('me/sendchildorder', views.SendChildOrderView.as_view(), name='getchats'),
    path('me/cancelchildorder', views.CancelChildOrderView.as_view(), name='getchats'),
    path('me/sendparentorder', views.SendParentOrderView.as_view(), name='getchats'),
    path('me/cancelparentorder', views.CancelParentOrderView.as_view(), name='getchats'),
    path('me/cancelallchildorders', views.CancelAllChildOrdersView.as_view(), name='getchats'),
    path('me/getchildorders', views.GetChildOrdersView.as_view(), name='getchats'),
    path('me/getparentorders', views.GetParentOrdersView.as_view(), name='getchats'),
    path('me/getparentorder', views.GetParentOrdersView.as_view(), name='getchats'),
    path('me/getexecutions', views.GetExecutionsView.as_view(), name='getchats'),
    path('me/getpositions', views.GetPositionsView.as_view(), name='getchats'),
    path('me/getcollateralhistory', views.GetCollateralHistoryView.as_view(), name='getchats'),
    path('me/gettradingcommission', views.GetTradingCommissionView.as_view(), name='getchats'),
]
