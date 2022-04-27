from turtle import update
from django.db import models




class TempUser(models.Model):
    username = models.CharField(max_length=32)##짧은 글귀를 저장하기 위해서
    email = models.CharField(max_length=32)##짧은 글귀를 저장하기 위해서

class Post(models.Model):##
    title = models.CharField(max_length=32)##짧은 글귀를 저장하기 위해서
    content = models.TextField(blank=True, null=True)##길이를 알 수 없는 글귀(장문위주)
    created_at = models.DateTimeField(auto_now_add=True)##시간과 관련된
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(
        TempUser, on_delete=models.CASCADE,
        blank=True, null=True
    )

    liked_users = models.ManyToManyField(
        TempUser,
        related_name="user_likes"
    )

    # likes = models.IntegerField(default=0) ##숫자와 관련된












