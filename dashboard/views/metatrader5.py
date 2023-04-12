from django.shortcuts import render
import MetaTrader5 as mt
from ..models import AccountInfo


#Initialize Metatrader5
if not mt.initialize():
    print('Initialization is needed')
else:
    print('Metatrader5 is initialized')

#Deriv_function
def get_Deriv_Data():

    # user login credential
    server = "MetaQuotes-Demo"
    login = 68457740
    password = "ejrkxc8n"

    mt.login(login, password, server)
    account_info = mt.account_info()

    #saving account info to database
    accountInfo1 = AccountInfo(
    login = account_info.login,
    balance = account_info.balance,
    equity = account_info.equity,
    )
    "".join(accountInfo1.save())
    return 


#getICMarketsEU function
def getICMarketsEU():

    # user login credential
    server = "MetaQuotes-Demo"
    login = 68457577
    password = "eb1ytbuz" 

    mt.login(login, password, server)
    account_info = mt.account_info()

    #saving account info to database
    accountInfo2 = AccountInfo.objects.create(
         login = account_info.login,
         balance = account_info.balance,
         equity = account_info.equity,
    )
    "".join(accountInfo2.save())
    return 

#getICMarketsEU1
def getICMarketsEU1():

    # user login credential
    server = "MetaQuotes-Demo"
    login = 68457670
    password = "r4yaxksx"

    mt.login(login, password, server)
    account_info = mt.account_info()

    #saving account info to database
    accountInfo3 = AccountInfo.objects.create(
        login = account_info.login,
        balance = account_info.balance,
        equity = account_info.equity
    )
    "".join(accountInfo3.save())
    return

    









