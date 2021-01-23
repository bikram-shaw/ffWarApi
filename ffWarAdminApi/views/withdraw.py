from rest_framework import viewsets, permissions,decorators,status
from ffWarUserApi.models.user import WithdrawModel, Wallet
from ffWarUserApi.models.game import TransactionModel
from rest_framework.response import Response
from ffWarAdminApi.serializers.gameSerializers import WithdrawReqSerializer, UserTransactionSerializer
from rest_framework.views import APIView

from ffWarUserApi.serializers import TransactionSerializer


@decorators.permission_classes([permissions.AllowAny])
class WithReqViewset(viewsets.ModelViewSet):
    queryset = WithdrawModel.objects.all()
    serializer_class = WithdrawReqSerializer
    def list(self, request, *args, **kwargs):
        wth_req=WithdrawModel.objects.filter(wth_status=False)
        print(wth_req)
        serializer=self.get_serializer(wth_req,many=True)
        return Response(serializer.data)



    def retrieve(self, request, *args, **kwargs):
        try:
           wth_data=WithdrawModel.objects.get(id=self.kwargs["pk"],wth_status=False)
           wth_data.wth_status = True
           wth_data.save()
        except WithdrawModel.DoesNotExist:
           return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("Success",status=status.HTTP_200_OK)

@decorators.permission_classes([permissions.AllowAny])
class RefundView(APIView):
    def post(self,request):
        wth_data = WithdrawModel.objects.get(id=request.data["id"], wth_status=False)
        wallet=Wallet.objects.get(user=wth_data.user)
        wallet.win_bal=wallet.win_bal+int(wth_data.wth_amount)
        wallet.save()
        wth_data.wth_status = True
        wth_data.save()
        print(request.data["description"])
        user_txn = UserTransactionSerializer(data={'user':wth_data.user.id, "txn_status": "credit",
                                                   "txn_description":"Refund :"+ request.data["description"],
                                                   "txn_amount": wth_data.wth_amount})

        if user_txn.is_valid():
            print(user_txn.validated_data)

            user_txn.save()
            return Response("success",status=status.HTTP_200_OK)
        return Response(user_txn.errors,status=status.HTTP_400_BAD_REQUEST)
@decorators.permission_classes([permissions.AllowAny])
class UserTxnHistory(APIView):
    def post(self,request):
        wth_data = WithdrawModel.objects.get(id=request.data["id"])

        txn=TransactionModel.objects.filter(user=wth_data.user.id)
        txn_seria=TransactionSerializer(txn,many=True)
        return Response(txn_seria.data,status=status.HTTP_200_OK)

