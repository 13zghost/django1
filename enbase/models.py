from django.db import models
from django.utils import timezone


class GameDomain(models.Model):
    domain = models.CharField(max_length=40)
    def __str__(self):
        return self.domain

class GameType(models.Model):
    type = models.CharField(max_length=40)
    def __str__(self):
        return self.type

class Game(models.Model):
  #  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    global_id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey("GameDomain",on_delete=models.CASCADE)
    local_id = models.IntegerField()
    type = models.ForeignKey("GameType",on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    quality = models.FloatField()
    scenario = models.BooleanField()
    date = models.CharField(max_length=20)
  #  title = models.CharField(max_length=200)
  #  text = models.TextField()
  #  created_date = models.DateTimeField(
  #          default=timezone.now)
  #  published_date = models.DateTimeField(
  #          blank=True, null=True)

    def publish(self):
  #      self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.global_id