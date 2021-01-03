from django.db import models
import uuid

class GameModel(models.Model):

    entry_fee=models.IntegerField()
    win_prize = models.CharField(max_length=200)
    map = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    per_kill = models.IntegerField()
    spots = models.IntegerField()
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    status = models.CharField(max_length=100)



class RoomDetailsModel(models.Model):
    room_id=models.CharField(max_length=100)
    room_pass=models.CharField(max_length=100)
    game_id=models.IntegerField()

class ResultModel(models.Model):
    kill=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    game_id=models.IntegerField()
    player_name=models.CharField(max_length=200)


