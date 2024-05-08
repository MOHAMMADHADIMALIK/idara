from django.db import models
# Create your models here.


class dropdownoptions(models.Model):
    id = models.AutoField(primary_key=True)
    cord = models.CharField(max_length=50,null=True)
    accounttype = models.CharField(max_length=50,null=True)
    ledgerhead = models.CharField(max_length=100, null=True)


class donation(models.Model):
    crorde = models.CharField(null=True, max_length=50)
    transitionid = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    ledgerhead = models.CharField(max_length=100, null=True)
    onoroff =  models.CharField(null=True, max_length=50)
    accounttype = models.CharField(max_length=50,null=True)
