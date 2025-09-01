from django.shortcuts import render
import stripe
from django.conf import settings
from rest_framework import views, generics, permissions, status, response
from .models import Transaction
from .serializers import TransactionSerializer, DepositSerializer

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

class DepositView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():

            try:
                # Create a new Stripe customer
                '''
                customer = stripe.Customer.create(
                    email=request.user.email,
                    source=serializer.validated_data['token']
                )'''

                # Create a new charge
                charge = stripe.Charge.create(
                    amount=int(serializer.validated_data['amount'] * 100),  # Amount in cents
                    currency='usd',
                    customer=customer.id,
                    source=serializer.validated_data['token'],
                    description=f'Deposit for {request.user.username}'
                )

                # Create a new transaction record
                #transaction = 
                
                Transaction.objects.create(
                    user=request.user,
                    amount=serializer.validated_data['amount'],
                    transaction_type='Deposit',
                    stripe_charge_id=charge.id,
                    status='completed'
                )

                return response.Response({'message':'Deposit successful'}, status=status.HTTP_200_OK)
            except stripe.error.StripeError as e:
                Transaction.objects.create(
                    user=request.user,
                    amount=serializer.validated_data['amount'],
                    status='failed',
                    transaction_type='deposit'
                )
                return response.Response({'message': 'Deposit failed', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionHistoryView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        transactions = Transaction.objects.filter(user=self.request.user).order_by('-timestamp')
        return transactions

    