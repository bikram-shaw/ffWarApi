from django.db import models
from ffWarUserApi.models.user import User
from django.conf import settings
class JoinGameModel(models.Model):
    user = models.ForeignKey(User,null=True,related_name='joingame', on_delete=models.CASCADE)
    game_id=models.IntegerField()
    pay_status=models.BooleanField(default=False)
    player_name=models.CharField(max_length=200)

class TransactionModel(models.Model):
    txn_status=models.CharField(max_length=200)
    txn_date=models.DateTimeField(auto_now_add=True)
    txn_description=models.CharField(max_length=200)
    txn_amount=models.IntegerField()
    user = models.ForeignKey(User, related_name='transaction',null=True, on_delete=models.CASCADE)

