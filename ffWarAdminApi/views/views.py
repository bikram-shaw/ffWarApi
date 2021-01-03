from ffWarAdminApi.serializers.gameSerializers import UserTransactionSerializer,ResultSerializer,GameSerializers,FetchJoinPlayerSerializer,RoomDetailsSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,decorators,permissions
from rest_framework.views import APIView
from ffWarAdminApi.models.gameModel import GameModel,RoomDetailsModel,ResultModel
from ffWarUserApi.models.game import JoinGameModel

from ffWarUserApi.models.user import Wallet,User
import uuid
# Create your views here.
@decorators.permission_classes([permissions.AllowAny])
class GameViewSet(viewsets.ModelViewSet):

    queryset = GameModel.objects.all()
    serializer_class = GameSerializers

@decorators.permission_classes([permissions.AllowAny])
class RoomDetailsViewSet(viewsets.ModelViewSet):
    queryset = RoomDetailsModel.objects.all()
    serializer_class = RoomDetailsSerializers
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
          try:
            gamemodal = GameModel.objects.get(id=request.data["game_id"],status='active')




            gamemodal.status='ongoing'
            gamemodal.save()
            serializer.save()
          except:
            return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


        return Response("Insert Success",status=status.HTTP_201_CREATED)
@decorators.permission_classes([permissions.AllowAny])
class FetchJoinPlayerView(APIView):
    def post(self,request):
        joinplayer=JoinGameModel.objects.filter(game_id=request.data["game_id"],pay_status=False)
        serializer=FetchJoinPlayerSerializer(joinplayer,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
@decorators.permission_classes([permissions.AllowAny])
class ResultView(APIView):
    def post(self,request):
        game_id=request.data["game_id"]
        for data in request.data["data"]:
            wallet=Wallet.objects.get(user=data["player_id"])
            wallet.win_bal=wallet.win_bal+int(data["amount"])
            wallet.save()
            joinPlayerPayStatus=JoinGameModel.objects.get(id=data["id"])
            joinPlayerPayStatus.pay_status=True
            joinPlayerPayStatus.save()
            user_txn=UserTransactionSerializer(data={'user': data["player_id"],"txn_status": "credit", "txn_description": "#" + str(game_id) + " Game Win",
                                          "txn_amount": data["amount"]
                                          })
            if user_txn.is_valid():
                print(user_txn.validated_data)
                user_txn.save()
                result=ResultSerializer(data={"kill":data["kill"],"amount":data["amount"],
                                              "player_name":data["player_name"],"game_id":game_id})
                if result.is_valid():
                    result.save()
                    game = GameModel.objects.get(id=game_id)
                    game.status='complete'
                    game.save()


        return Response(status=status.HTTP_201_CREATED)

