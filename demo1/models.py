from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def name_min(data):
    if len(data) <=2:
        raise ValidationError("长度不够，必须两位以上",params={'value': data})


class Goods(models.Model):
    name = models.CharField(max_length=200,validators=[])
    time = models.DateTimeField(auto_now=True,blank=True)




class User(models.Model):
    name = models.CharField(validators=[name_min],max_length=20,default="张三")
    sex = models.IntegerField(choices=(
        (1,'男'),
        (2,'女')
    ),error_messages={'null':'no null','blank':'no blank'}
    )
