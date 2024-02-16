from django.db import models
from django.contrib.auth.models import User

#question model
class Question(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField( max_length=300)
    detail =models.TextField()
    created_at = models.DateField(auto_now_add = True)

#answer model 
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
       return self.detail

#comment model 
class Comment(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'comment_user')
    created_at = models.DateTimeField(auto_now_add = True)

#upvote model 
class UpVote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'upvote_user')

#downvote model
class DownVote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'downvote_user')
    