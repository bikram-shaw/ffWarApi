from rest_framework import viewsets, permissions,decorators,status
from rest_framework.views import APIView
from ffWarUserApi.serializers.serializers import WalletSerializer,TransactionSerializer,WithdrawSerializer
from ffWarUserApi.models import Wallet,TransactionModel,WithdrawModel
from rest_framework.response import Response

@decorators.permission_classes([permissions.AllowAny])
class WalletViewset(APIView):
    def get(self,request):
        wallet=Wallet.objects.get(user=request.user)
        serializer=WalletSerializer(wallet)
        return Response(serializer.data)

@decorators.permission_classes([permissions.AllowAny])
class GetUserTransaction(APIView):
    def get(self,request):
        user_txn=TransactionModel.objects.filter(user=request.user).order_by('txn_date')[::-1]
        serializer=TransactionSerializer(user_txn,many=True)
        return Response(serializer.data)

@decorators.permission_classes([permissions.AllowAny])
class PostUserTransaction(APIView):
    def post(self, request):

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@decorators.permission_classes([permissions.AllowAny])
class WithdrawViewset(APIView):
    def post(self,request):

        user_wal=Wallet.objects.get(user=request.user)
        if user_wal.win_bal>=int(request.data['wth_amount']):
            user_wal.win_bal=user_wal.win_bal-int(request.data['wth_amount'])
            user_wal.save()
            serializer = WithdrawSerializer(data=request.data)
            if serializer.is_valid():
                withdraw=serializer.save()
                withdraw.user=request.user
                withdraw.save()
                txn = TransactionSerializer(data={"txn_status": "debit", "txn_description": "withdraw",
                                                  "txn_amount":request.data['wth_amount']})
                if txn.is_valid():

                    user_txn=txn.save()
                    user_txn.user=request.user
                    user_txn.save()


                return Response("Withdraw Success !<br>Amount will be credited into 48 hours",status=status.HTTP_201_CREATED)

        return Response("Low Balance", status=status.HTTP_400_BAD_REQUEST)







