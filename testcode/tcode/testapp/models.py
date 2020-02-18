from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

### 서버실 테스트 서버 관리대장(RP)
class Serverlist(models.Model):
    ##id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500) #소유자명
    team = models.CharField(max_length=500) #소속팀
    server_count = models.IntegerField() #보유댓수
    model_name = models.CharField(max_length=500) #서버 모델명
    code = models.CharField(max_length=500) #분류코드
    use_case = models.TextField(max_length=5000) #사용용도
    created_date = models.DateTimeField(default=timezone.now) #입력일시
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)  #등록일시

    #def publishd_date (self):
    #    self.published_date = timezone.now()
    #     self.save()

    #def __str__(self):
    #    return self.name







    









    


    
    




