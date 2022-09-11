from django.urls import path, re_path
from .views import DidTheyMoveView, CheckMovedView

urlpatterns = [
    path('didTheyMove/', DidTheyMoveView.as_view({'get': 'list'}), name="didTheyMove"),
    re_path('checkMoved/(?P<client_name>\D+)/', CheckMovedView.as_view(), name="checkMoved")
]