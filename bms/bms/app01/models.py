from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField('serial_num', primary_key=True)
    name = models.CharField('name',max_length=64 )
    addr = models.CharField('address',max_length=64)
    created_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField('serial_num', primary_key=True)
    name = models.CharField('name', max_length=64, null=True)
    ISBN = models.CharField('ISBN', max_length=64)
    traslator = models.CharField('translator', max_length=64)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)

class Author(models.Model):
    id = models.AutoField('serail_num',primary_key=True)
    name = models.CharField('name', max_length=64)
    sex =models.CharField('sex', max_length=4)
    age = models.IntegerField('age', default=0)
    tel = models.CharField('Telephone', max_length=64)
    book = models.ManyToManyField(to=Book)

class LMSUser(models.Model):
    id = models.AutoField('serial_num', primary_key=True)
    username = models.CharField('username', max_length=32)
    password = models.CharField('password', max_length=32)
    email = models.EmailField('Email')
    mobile = models.IntegerField('telephone', max_length=11)
