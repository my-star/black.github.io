from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(verbose_name='username', max_length=20)
    emp_num = models.IntegerField(verbose_name='employee_number',unique=True)
    password = models.CharField(verbose_name='password', max_length=64)

    def __str__(self):
        return '{}{}'.format(self.user_name, self.emp_num)

class Type(models.Model):
    type_name = models.CharField(verbose_name='GOOdsType',max_length=50)

    def __str__(self):
        return self.type_name

class Goods(models.Model):
    type = models.ForeignKey(to=Type,on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=200)
    goods_count = models.IntegerField()
    position = models.CharField(max_length=50)
    comment = models.CharField(max_length=200,null=True)
    record_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

class Log(models.Model):
    user = models.CharField(max_length=30)
    goods_type = models.CharField(max_length=30,null=True)
    goods_name = models.CharField(max_length=50,null=True)
    operation = models.CharField(max_length=30)
    record_date = models.DateField(auto_now_add=True)