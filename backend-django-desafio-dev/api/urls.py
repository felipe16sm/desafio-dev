from django.urls import re_path

from .views import (
    StoreBulkTransactionView,
    StoreRetrieveCreateTransactionView,
    StoreListCreateView,
)

urlpatterns = [
    re_path(r"^stores/?$", StoreListCreateView.as_view()),
    re_path(r"^stores/transactions/?$", StoreBulkTransactionView.as_view()),
    re_path(
        r"^stores/(?P<pk>\w+)/transactions/?$",
        StoreRetrieveCreateTransactionView.as_view(),
    ),
]
