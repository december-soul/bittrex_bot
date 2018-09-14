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
