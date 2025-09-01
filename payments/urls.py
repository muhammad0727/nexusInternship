from django.urls import path
from .views import DepositView, TransactionHistoryView

urlpatterns = [
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('history/', TransactionHistoryView.as_view(), name='transaction-history'),
]
