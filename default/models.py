from django.db import models

# Create your models here.
class Poll(models.Model):
    subject = models.CharField("投票主題",max_length=64)
    #subject:主題
    #裡面最多可以放幾個字(必要)
    #charfield 單行 TextField多行
    desc = models.TextField("說明")
    #desc:說明欄位
    created = models.DateField("建立日期",auto_now_add=True)

    def __str__(self):
        return self.subject

class Option(models.Model):
    title = models.CharField("選項文字",max_length=64)
    votes = models.IntegerField("票數",default=0)
    poll_id = models.IntegerField("投票主題編號")

    def __str__(self):
        return f"{self.poll_id} - {self.title} : {self.votes}"
        

    
