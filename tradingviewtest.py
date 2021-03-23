from tradingview_ta import TA_Handler, Interval, Exchange
from queue import Queue
import time
import requests


API_KEY = '1702676070:AAHhPM13I4CToK2iq8R23tEpwY2u-ESrEwU'

Future_coins = ["BTCUSDTPERP", "ETHUSDTPERP", "XRPUSDTPERP", "ONEUSDTPERP", "BNBUSDTPERP", "ADAUSDTPERP", "THETAUSDTPERP", "DOTUSDTPERP",
"TRXUSDTPERP", "LTCUSDTPERP", "UNIUSDTPERP","CHZUSDTPERP", "VETUSDTPERP", "SXPUSDTPERP", "EOSUSDTPERP", "XLMUSDTPERP", "AVAXUSDTPERP",
"SOLUSDTPERP", "BCHUSDTPERP", "LINKUSDTPERP", "SFPUSDTPERP", "LUNAUSDTPERP", "FILUSDTPERP", "FILUSDTPERP", "ENJUSDTPERP", "SUSHIUSDTPERP", 
"KSMUSDTPERP", "MKRUSDTPERP", "BATUSDTPERP", "IOSTUSDTPERP", "COTIUSDTPERP", "ONTUSDTPERP", "1INCHUSDTPERP", "FTMUSDTPERP", "TRBUSDTPERP",
"TOMOUSDTPERP", "ETCUSDTPERP", "AAVEUSDTPERP", "RSRUSDTPERP", "ALPHAUSDTPERP", "ANKRUSDTPERP", "KNCUSDTPERP", "XTZUSDTPERP", "GRTUSDTPERP", 
"KAVAUSDTPERP", "IOTAUSDTPERP", "NEOUSDTPERP", "SANDUSDTPERP", "CRVUSDTPERP", "OCEANUSDTPERP", "ATOMUSDTPERP", "DOGEUSDTPERP", "EGLDUSDTPERP", 
"ALGOUSDTPERP", "SRMUSDTPERP", "CVCUSDTPERP", "ZILUSDTPERP", "BELUSDTPERP", "RVNUSDTPERP", "YFIUSDTPERP", "SKLUSDTPERP", "CHRUSDTPERP", 
"QTUMUSDTPERP", "MATICUSDTPERP", "MANAUSDTPERP", "COMPUSDTPERP", "CTKUSDTPERP", "XEMUSDTPERP", "BANDUSDTPERP", "ALICEUSDTPERP", "HNTUSDTPERP",
"REEFUSDTPERP", "AKROUSDTPERP", "ZRXUSDTPERP", "OMGUSDTPERP", "ZECUSDTPERP", "NEARUSDTPERP", "DASHUSDTPERP", "WAVESUSDTPERP", "SNXUSDTPERP", 
"RENUSDTPERP", "HBARUSDTPERP", "RLCUSDTPERP", "STORJUSDTPERP", "ICXUSDTPERP", "BALUSDTPERP", "DODOUSDTPERP", "LITUSDTPERP", "BTSUSDTPERP", 
"AXSUSDTPERP", "BLZUSDTPERP", "FLMUSDTPERP", "ZENUSDTPERP", "BZRXUSDTPERP", "RUNEUSDTPERP", "YFIIUSDTPERP", "LRCUSDTPERP", "UNFIUSDTPERP", 
"DEFIUSDTPERP"] 


Future_coins_test = ["BTCUSDTPERP", "ETHUSDTPERP", "XRPUSDTPERP", "ONEUSDTPERP", "BNBUSDTPERP", "ADAUSDTPERP", "THETAUSDTPERP", "DOTUSDTPERP",
"TRXUSDTPERP"] 



class out_coins:
    def __init__(self, coin):
        self.coin = coin
        self.EMA10 = [0,0,0,0,0,0]
        self.EMA20 = [0,0,0,0,0,0]


    def add2EMA10(self,price):
        for i in range(5):
            self.EMA10[i] = self.EMA10[i+1]
        self.EMA10[5] = price

    def add2EMA20(self,price):
        for i in range(5):
            self.EMA20[i] = self.EMA20[i+1]
        self.EMA20[5] = price
    
    # def getEMA10(self, index):
    #     return self.EMA10[index]
    
    # def getEMA20(self, index):
    #     return self.EMA20[index]

    def lastless(self):
        if self.EMA10[5] < self.EMA20[5]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] < self.EMA20[4]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] < self.EMA20[3]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] < self.EMA20[2]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] == self.EMA20[2] and self.EMA10[1] < self.EMA20[1]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] == self.EMA20[2] and self.EMA10[1] == self.EMA20[1]  and self.EMA10[0] < self.EMA20[0]:
            return True
        return False

    def lastmore(self):
        if self.EMA10[5] > self.EMA20[5]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] > self.EMA20[4]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] > self.EMA20[3]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] > self.EMA20[2]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] == self.EMA20[2] and self.EMA10[1] > self.EMA20[1]:
            return True
        elif self.EMA10[5] == self.EMA20[5] and self.EMA10[4] == self.EMA20[4] and self.EMA10[3] == self.EMA20[3] and self.EMA10[2] == self.EMA20[2] and self.EMA10[1] == self.EMA20[1]  and self.EMA10[0] > self.EMA20[0]:
            return True
        return False


def main():
    pre_dict = dict() 
    yet15 = False
    for coin in Future_coins:
        pre_dict[coin] = out_coins(coin)
    while(True):
        start = time.time()
        out_coins_long = []
        out_coins_short = []
        exeptions = 0
        for coin in Future_coins:
            print(coin)
            handler = TA_Handler(
                symbol=coin,
                screener="crypto",
                exchange="binance",
                interval=Interval.INTERVAL_15_MINUTES
            )
            try:
                analysis = handler.get_analysis()
                if analysis.indicators["EMA10"] > analysis.indicators["EMA20"] and pre_dict[coin].lastless():
                    out_coins_long.append(coin)
                if analysis.indicators["EMA10"] < analysis.indicators["EMA20"] and pre_dict[coin].lastmore():
                    out_coins_short.append(coin)
                # if yet15 == True:
                pre_dict[coin].add2EMA10(analysis.indicators["EMA10"])
                pre_dict[coin].add2EMA20(analysis.indicators["EMA20"])
                #     yet15 = False
                # else:
                #     yet15 = True
                time.sleep(1)
            except:
                print("exept   " + coin)
                exeptions += 1

        print(exeptions)
        strshort = "short\n"
        for coin_sh in out_coins_short:
            strshort = strshort + coin_sh + "\n"
        strlong = "long\n"
        for coin_l in out_coins_long:
            strlong = strlong + coin_l + "\n"
        out = strlong + strshort
        url = "https://api.telegram.org/bot1702676070:AAHhPM13I4CToK2iq8R23tEpwY2u-ESrEwU/sendMessage?chat_id=@fireborntest&text=" + out
        requests.post(url)
        end = time.time()
        # time.sleep(450-end+start)
        




if __name__ == "__main__":
	main()
