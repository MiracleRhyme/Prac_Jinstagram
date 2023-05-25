from django.db import models

# Create your models here.
class Feed(models.Model):
    content       = models.TextField() # 글내용
    image         = models.TextField() # 피드 이미지
    # profile_image = models.TextField() # 프로필 이미지
    # user_id       = models.TextField() # 글쓴이
    email         = models.EmailField(default='') # 이메일 주소

class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)

class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()

class BookMark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)