import time
import pyupbit

#1분 단위로, 가격중 제일 높은 가격과 낮은 가격을 찾는다.
topprice = pyupbit.get_current_price("KRW-DOGE")
rowprice = pyupbit.get_current_price("KRW-DOGE")
buyprice = 0
check = 0
buycoin = False
hasmymoney = 100000
upprice=3.00
fee = 0.0005
check_price_min = 5
ea = 0
access="IErYNgo9YrFnUqYYXecJE7OxkUzmzk1CgVryg6ee"
secret="psumaP4D7af2A9MMfRAXatzuMrx4TvkPLNyli08Q"
upbit = pyupbit.Upbit(access, secret)
inittime_sec = 3600
while (True):
    price = pyupbit.get_current_price("KRW-DOGE")
    time.sleep(0.5)
    check = check + 1

    #초기화 시간 전에 코인을 못팔면 다시 거래를 시작한다.
    if (check > inittime_sec):
        topprice = pyupbit.get_current_price("KRW-DOGE")
        rowprice = pyupbit.get_current_price("KRW-DOGE")
        buycoin = False
        check = 0

    if (buycoin == False):
        if (price > topprice):
            topprice = price

        if (price < rowprice):
            rowprice = price        


        
        #낮은 가격이 나오면 코인을 삽니다.
        if (check > ( (check_price_min * 60) / 2)):
            print("set buyprice:{}".format(rowprice))
            if (price <= rowprice):
                ea = 5500 / price
                upbit.buy_market_order("KRW-DOGE", 5500)
                print('buy done . {}'.format(price))
                buyprice = rowprice
                buycoin = True

    if (buycoin == True):
        hope_buy_price = buyprice + upprice
        print('buypriceJ:{}, curprice:{}'.format(hope_buy_price, price))
        if ( price >= hope_buy_price ):
            print('sell doen . {}'.format(price))
            upbit.sell_market_order("KRW-DOGE", ea)
            check = 0
            buycoin = False

    
