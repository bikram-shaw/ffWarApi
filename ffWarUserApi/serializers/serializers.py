from rest_framework import serializers
from ffWarUserApi.models import User,Wallet,JoinGameModel,TransactionModel,WithdrawModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransactionModel
        fields=('txn_status','txn_date','txn_description','txn_amount')

class joinGameSerializer(serializers.ModelSerializer):

    class Meta:
        model=JoinGameModel
        fields=('id','game_id','player_name')







class WalletSerializer(serializers.ModelSerializer):
    #user=UserSerializer(many=False)
    class Meta:
        model= Wallet
        fields = ('wal_bal','win_bal')

class UserSerializer(serializers.ModelSerializer):
    wallet=WalletSerializer(read_only=True,many=False)



    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
class WithdrawSerializer(serializers.ModelSerializer):

    class Meta:
        model=WithdrawModel
        fields="__all__"
class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email','name', 'mobile', 'is_staff', 'is_superuser')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser')


class EmptySerializer(serializers.Serializer):
    pass

