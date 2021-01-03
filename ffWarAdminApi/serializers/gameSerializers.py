from rest_framework import serializers
from ffWarAdminApi.models.gameModel import GameModel,RoomDetailsModel,ResultModel
from ffWarUserApi.models.user import WithdrawModel
from ffWarUserApi.models.game import JoinGameModel, TransactionModel


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields ="__all__"

class RoomDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model= RoomDetailsModel
        fields='__all__'

class WithdrawReqSerializer(serializers.ModelSerializer):

    class Meta:
        model=WithdrawModel
        fields=("id","wth_amount","wth_method","wth_date")

class FetchJoinPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=JoinGameModel
        fields='__all__'
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResultModel
        fields='__all__'
class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransactionModel
        fields="__all__"