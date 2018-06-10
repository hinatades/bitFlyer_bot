from django.urls import path, include
from . import views

 
urlpatterns = [
    path('', views.TradingView.as_view(), name='get'),
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
]
