# bittrex_bot
bittrex SL TP Stoploss Takeprofit trading bot

# Usage
 trade.py --coin=<COINNAME> --quantity=<QUANTITY> --takeprofit=<TAKEPROFIT> --stoploss=<STOPLOSS>

    Example:
          trade.py --coin=ETH --quantity=0.1 --takeprofit=0.052 --stoploss=0.045
                         This will sell 0.1 ETH at 0.052 ETH/BTC or 0.045 ETH/BTC

    --coin : the coin you would like to soll. Allways a BTC traiding pair

    --takeprofit: if the current price is above this value, then it will be sold

    --stoploss: if the current price is below this value, then it will be sold

    --quantity : how many coins you would like to sell? you mast hold

    --tryrun : do not sell any coins, use try run

# Install
edit the trading.py file to add your bittrex key and secret. This must allow trading
