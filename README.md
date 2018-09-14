# bittrex_bot
bittrex SL TP Stoploss Takeprofit trading bot

# Usage
 trade.py --coin=<COINNAME> --quantity=<QUANTITY> --takeprofit=<TAKEPROFIT> --stoploss=<STOPLOSS>

    Example:
          trade.py --coin=ETH --quantity=0.1 --takeprofit=0.052 --stoploss=0.045 --tryrun
                         This will sell 0.1 ETH at 0.052 ETH/BTC or 0.045 ETH/BTC

          trade.py --coin=ETH --quantity=0.1 --takeprofit=0.059 --stoploss=0.045 --trailingstopstart=0.052 --trailingstopstep=0.002
                         This will sell 0.1 ETH at 0.059 ETH/BTC or 0.045 ETH/BTC, SL will be trailed in 0.002 steps

    --coin : the coin you would like to soll. Allways a BTC traiding pair

    --takeprofit: if the current price is above this value, then it will be sold

    --stoploss: if the current price is below this value, then it will be sold

    --trailingstopstart : define a start price where we switch from normal SL to trailing stop loos")

    --trailingstopstep : if trailing stop loos is aktive then the SL is trailed so many points behind the highest value

    --quantity : how many coins you would like to sell? you mast hold

    --tryrun : do not sell any coins, use try run

# Install
edit the trading.py file to add your bittrex key and secret. This must allow trading

# Output
```
python trade.py --coin=ETH --quantity=0.1 --takeprofit=0.049 --stoploss=0.029 --trailingstopstart=0.03194 --trailingstopstep=0.0002 --tryrun

[+] handle BTC-ETH

[+] number of coins to sell 0.10000000 ETH

[+] Takeprofit set to 0.04900000 BTC/ETH

[+] Stop Loss set to 0.02900000 BTC/ETH

[+] Traling Stop will start at 0.03194000 BTC/ETH

[+] Traling Stop will move Stop Loss 0.00020000 steps after the current price

Enter "go" to continue. WARNING!!! CONTINUE ON YOUR OWN RISK AND ONLY IF YOU KNOW WHAT WILL HAPPEN!!!
go

2018-09-14 15:28:34    ETH Current Price: 0.03183997 BTC (TP=0.04900000, SL=0.02900000)

...

2018-09-14 15:41:51    ETH Current Price: 0.03193453 BTC (TP=0.04900000, SL=0.02900000)

2018-09-14 15:41:53    ETH Current Price: 0.03195140 BTC (TP=0.04900000, SL=0.02900000)
>>TrailingStop: new stop loos reached. current price 0.03195140 BTC, old SL=0.02900000 TrailingStopSteps=0.00020000 new SL=0.03175140

2018-09-14 15:41:55    ETH Current Price: 0.03195140 BTC (TP=0.04900000, SL=0.03175140)

2018-09-14 15:41:57    ETH Current Price: 0.03195140 BTC (TP=0.04900000, SL=0.03175140)

...

2018-09-14 15:42:27    ETH Current Price: 0.03187241 BTC (TP=0.04900000, SL=0.03175140)

2018-09-14 15:42:29    ETH Current Price: 0.03199592 BTC (TP=0.04900000, SL=0.03175140)
>>TrailingStop: new stop loos reached. current price 0.03199592 BTC, old SL=0.03175140 TrailingStopSteps=0.00020000 new SL=0.03179592

2018-09-14 15:42:31    ETH Current Price: 0.03199592 BTC (TP=0.04900000, SL=0.03179592)

2018-09-14 15:42:33    ETH Current Price: 0.03199592 BTC (TP=0.04900000, SL=0.03179592)
```
