from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30) #username аккаунта
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default=None)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)  # название поста
    content = models.TextField()  # содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # автоматическое прописание времени публикации