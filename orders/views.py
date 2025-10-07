from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shorcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-order_date')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'],url_path='cancel')
    def cancel_order(self,request,pk=None):
        order = get_object_or_404(Order,pk=pk)

        if order.status in ['C','L']:
            return Response(
                {'detail':f"Order {pk} cannot be cancelled because its stats}"
                ,status = status.HTTP_400_BAD_REQUEST
            )
            order.status = 'C'
            order.save(update_fields=['status'])
            serializer = self.get_serializer(order)
            return Response(serializer.data,status=HTTP_200_OK)