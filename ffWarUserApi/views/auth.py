from ffWarUserApi.serializers.serializers import UserSerializer,WalletSerializer,TransactionSerializer, UserLoginSerializer, AuthUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import decorators,permissions
from authentication import Authentication
from ffWarUserApi.models import Wallet
@api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def userSignUp(request):
    if request.method == 'POST':

        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            save=serializer.save()
            auth = Authentication()
            user, token = auth.authenticate(serializer.validated_data.get('mobile'), serializer.validated_data.get('password'))
            data = AuthUserSerializer(user).data
            result = {'token': token}
            result.update(data)
            wallet=WalletSerializer(data={'win_bal':'0','wal_bal':'10'})
            if wallet.is_valid():
                user_wallet=wallet.save()
                user_wallet.user=save
                user_wallet.save()
                user_txn=TransactionSerializer(data={'txn_status':'credit','txn_amount':'10','txn_description':
                                                     'Signup bonus'})
                if user_txn.is_valid():

                    user_txn1=user_txn.save()
                    user_txn1.user=save
                    user_txn1.save()



            return Response(data=result,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def userSignIn(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            auth = Authentication()
            user, token = auth.authenticate(**serializer.validated_data)
            data = AuthUserSerializer(user).data
            result = {'token': token}
            result.update(data)
            return Response(data=result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)