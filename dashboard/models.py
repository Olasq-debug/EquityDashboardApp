from mongoengine import *
import time


# Create your models here.

class AccountInfo(Document):
    login = IntField()
    balance = FloatField()
    equity = FloatField()
    timestamps = DateField(default = time.strftime("%H:%M:%S"))

    def __str__(self):
        return self.login
