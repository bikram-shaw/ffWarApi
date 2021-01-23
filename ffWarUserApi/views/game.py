from ffWarAdminApi.models import GameModel,ResultModel
from ffWarUserApi.models import JoinGameModel,Wallet
from rest_framework import  permissions,decorators
from ffWarAdminApi.serializers import GameSerializers
from ffWarUserApi.serializers import joinGameSerializer,TransactionSerializer
from rest_framework import mixins,generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
@decorators.permission_classes([permissions.AllowAny])
class ActiveGameView(APIView):

    def get(self,request):
        active_games = GameModel.objects.filter(status='active')
        serializer = GameSerializers(active_games, many=True)
        i = 0;
        for data in serializer.data:


            join_spot = JoinGameModel.objects.filter(game_id=data["id"]).count()
            res={'join_spot':join_spot}

            serializer.data[i].update(res)
            i += 1

        return Response(serializer.data)

@decorators.permission_classes([permissions.AllowAny])
class OngoingGameView(APIView):
    def get(self, request):
        active_games = GameModel.objects.filter(status='ongoing')
        serializer = GameSerializers(active_games, many=True)
        i = 0;
        for data in serializer.data:
            join_spot = JoinGameModel.objects.filter(game_id=data["id"]).count()
            res = {'join_spot': join_spot}

            serializer.data[i].update(res)
            i += 1

        return Response(serializer.data)

@decorators.permission_classes([permissions.AllowAny])
class FetchJoinPlayerView(APIView):
    def post(self,request):

        joinUser = JoinGameModel.objects.filter(game_id=request.data["game_id"])
        serializer=joinGameSerializer(joinUser,many=True)
        return Response(serializer.data)
def join_game_service(request,game):
    serializer = joinGameSerializer(data=request.data)
    if serializer.is_valid():
        join_user = serializer.save()
        join_user.user = request.user

        join_user.save()

        txn = TransactionSerializer(data={"txn_status": "debit", "txn_description": "#" + str(game.id) + " Join Game",
                                          "txn_amount": game.entry_fee,
                                          'user': request.user.id})
        if txn.is_valid():
            txn.save()
        return Response(status=status.HTTP_201_CREATED)

@decorators.permission_classes([permissions.AllowAny])
class JoinGameView(APIView):
    def post(self,request):
        join_spot=JoinGameModel.objects.filter(game_id=request.data["game_id"]).count()
        game=GameModel.objects.get(id=request.data["game_id"])
        wallet=Wallet.objects.get(user=request.user.id)


        if((wallet.wal_bal>=game.entry_fee or wallet.win_bal>=game.entry_fee or wallet.win_bal+wallet.wal_bal>=game.entry_fee) and
        game.spots>join_spot):
            if wallet.wal_bal>=int(game.entry_fee):

                wallet.wal_bal=wallet.wal_bal - int(game.entry_fee)
                wallet.save()
                return join_game_service(request,game)

            elif wallet.wal_bal+wallet.win_bal>=int(game.entry_fee):


                remain_entry_fee=int(game.entry_fee-wallet.wal_bal)
                wallet.wal_bal = 0
                wallet.win_bal=wallet.win_bal-remain_entry_fee
                wallet.save()
                return join_game_service(request,game)
            else:

                wallet.win_bal=wallet.win_bal - int(game.entry_fee)
                wallet.save()
                return join_game_service(request,game)








        return Response("Low Balance",status=status.HTTP_400_BAD_REQUEST)
@decorators.permission_classes([permissions.AllowAny])
class CompletedGameView(APIView):
    def get(self, request):
        active_games = GameModel.objects.filter(status='complete')
        serializer = GameSerializers(active_games, many=True)
        i = 0;
        for data in serializer.data:
            join_spot = JoinGameModel.objects.filter(game_id=data["id"]).count()
            res = {'join_spot': join_spot}

            serializer.data[i].update(res)
            i += 1

        return Response(serializer.data)

@decorators.permission_classes([permissions.AllowAny])
class FetchResultView(APIView):
    def post(self,request):

        result = ResultModel.objects.filter(game_id=request.data["game_id"])
        serializer=joinGameSerializer(result,many=True)
        return Response(serializer.data)



















