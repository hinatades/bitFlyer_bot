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
    path('you/getpermissions', views.GetPerissionsView.as_view(), name='ticker'),
    path('you/getbalance', views.GetBalanceView.as_view(), name='getexecutions'),
    path('you/getcollateral', views.GetCollateralView.as_view(), name='executions'),
    path('you/getcollateralaccounts', views.GetCollateralAccountsView.as_view(), name='getboardstate'),
    path('you/getaddresses', views.GetAddressesView.as_view(), name='gethealth'),
    path('you/getcoinins', views.GetCoinIns.as_view(), name='getchats'),
    path('you/getcoinouts', views.GetCoinOutsView.as_view(), name='executions'),
    path('you/getbankaccounts', views.GetBankAccountsView.as_view(), name='getboardstate'),
    path('you/getdeposits', views.GetDepositsView.as_view(), name='gethealth'),
    path('you/getwithdrawals', views.GetWithdrawalsView.as_view(), name='getchats'),
    path('you/sendchildorder', views.SendChildOrderView.as_view(), name='getchats'),
    path('you/cancelchildorder', views.CancelChildOrderView.as_view(), name='getchats'),
    path('you/sendparentorder', views.SendParentOrderView.as_view(), name='getchats'),
    path('you/cancelparentorder', views.CancelParentOrderView.as_view(), name='getchats'),
    path('you/cancelallchildorders', views.CancelAllChildOrdersView.as_view(), name='getchats'),
    path('you/getchildorders', views.GetChildOrdersView.as_view(), name='getchats'),
    path('you/getparentorders', views.GetParentOrdersView.as_view(), name='getchats'),
    path('you/getparentorder', views.GetParentOrderView.as_view(), name='getchats'),
    path('you/getexecutions', views.GetExecutionsView.as_view(), name='getchats'),
    path('you/getpositions', views.GetPositionsView.as_view(), name='getchats'),
    path('you/getcollateralhistory', views.GetCollateralHistoryView.as_view(), name='getchats'),
    path('you/gettradingcommission', views.GetTradingCommissionView.as_view(), name='getchats'),
]
