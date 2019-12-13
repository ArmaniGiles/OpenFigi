from django.db import models
from django.forms import ModelForm

class UniqueTableIdenfiers(models.Model):
    ticker = models.CharField(max_length=200, null=True) 
    name = models.CharField(max_length=200, null=True)
    marketSector = models.CharField(max_length=200, null=True)
    securityType = models.CharField(max_length=200, null=True)
    exchCode = models.CharField(max_length=200, null=True)
    timeStamp = models.DateTimeField()

    class Meta:
        abstract = True #Abtract Class

class Isin(UniqueTableIdenfiers):
    pass

class Sedol(UniqueTableIdenfiers):
    pass

#             .
#             .
#             .

class Cusip(UniqueTableIdenfiers):
    cusipCode = models.CharField(max_length=200)

    def __str__(self):
        return self.cusipCode

class CusipForm(ModelForm):

    class Meta:
        model = Cusip
        fields = ['cusipCode']


