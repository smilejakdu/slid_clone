from django.urls import path
from product.views import ProductView

urlpatterns = [
    path('', ProductView.as_view()),
]

