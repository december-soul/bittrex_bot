#get the system
import sys, signal, time, getopt, math
import datetime
from bittrex import bittrex

#API details
key  = '<ADD YOUR KEY>'
secret = '<ADD YOUR SECRET>'

api = bittrex(key, secret)

#goodbye~
def sigint_handler(signum, frame):
    print('\n[!] Escaped! Goodbye<3')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def printUsage():
    print("Usage:")
    print(" trade.py --coin=<COINNAME> --quantity=<QUANTITY> --takeprofit=<TAKEPROFIT> --stoploss=<STOPLOSS>")
    print("\n    Example:")
    print("          trade.py --coin=ETH --quantity=0.1 --takeprofit=0.052 --stoploss=0.045 --tryrun")
    print("                         This will sell 0.1 ETH at 0.052 ETH/BTC or 0.045 ETH/BTC\n")
    print("          trade.py --coin=ETH --quantity=0.1 --takeprofit=0.059 --stoploss=0.045 --trailingstopstart=0.052 --trailingstopstep=0.002")
    print("                         This will sell 0.1 ETH at 0.059 ETH/BTC or 0.045 ETH/BTC, SL will be trailed in 0.002 steps\n")
    print("\n    --coin : the coin you would like to soll. Allways a BTC traiding pair")
    print("\n    --takeprofit: if the current price is above this value, then it will be sold")
    print("\n    --stoploss: if the current price is below this value, then it will be sold")
    print("\n    --quantity : how many coins you would like to sell? you mast hold")
    print("\n    --trailingstopstart : define a start price where we switch from normal SL to trailing stop loos")
    print("\n    --trailingstopstep : if trailing stop loos is aktive then the SL is trailed so many points behind the highest value")
    print("\n    --tryrun : do not sell any coins, use try run")
    sys.exit(2)

try:
    opts, args = getopt.getopt(sys.argv[1:],"hl:p:c:q:t",["help", "stoploss=", "takeprofit=", "coin=", "quantity=", "tryrun", "trailingstopstart=", "trailingstopstep="])
except getopt.GetoptError as err:
    print("getopt error")
    print(err)
    printUsage()

coin = "missing"
quantity = float('nan')
tp = float('nan')
sl = float('nan')
trailing_stop_step = float('nan')
trailing_stop_start = float('nan')

tryrun = False

for opt, arg in opts:
    if opt == '-h':
        printUsage()
    elif opt in ("-l", "--stoploss"):
        sl = float(arg)
    elif opt in ("--trailingstopstart"):
        trailing_stop_start = float(arg)
    elif opt in ("--trailingstopstep"):
        trailing_stop_step = float(arg)
    elif opt in ("-p", "--takeprofit"):
        tp = float(arg)
    elif opt in ("-c", "--coin"):
        coin = arg.upper()
    elif opt in ("-q", "--quantity"):
        quantity = float(arg)
    elif opt in ("-t", "--tryrun"):
        trynrun = True
    else:
        print("unknown option {}".format(opt))
        printUsage()

if math.isnan(sl):
    print("you need to define an stoploss {}".format(sl))
    printUsage()
    sys.exit(2)
if math.isnan(tp):
    print("you need to define an takeprofit")
    printUsage()
    sys.exit(2)
if math.isnan(quantity):
    print("you need to define an quantity")
    printUsage()
    sys.exit(2)
if not math.isnan(trailing_stop_step) and math.isnan(trailing_stop_start):
    print("you defined traling stop but missed trailingstopstart")
    printUsage()
    sys.exit(2) 
if math.isnan(trailing_stop_step) and not math.isnan(trailing_stop_start):
    print("you defined traling stop but missed trailingstopstep")
    printUsage()
    sys.exit(2) 
if coin == "missing":
    print("you need to define a coin")
    printUsage()
    sys.exit(2) 

print('\n[+] handle BTC-{}'.format(coin))
print('\n[+] number of coins to sell {:02.8f} {}'.format(quantity, coin))
print('\n[+] Takeprofit set to {:02.8f} BTC/{}'.format(tp,coin))
print('\n[+] Stop Loss set to {:02.8f} BTC/{}'.format(sl,coin))
if not math.isnan(trailing_stop_start) and not math.isnan(trailing_stop_step):
    print('\n[+] Traling Stop will start at {:02.8f} BTC/{}'.format(trailing_stop_start,coin))
    print('\n[+] Traling Stop will move Stop Loss {:02.8f} steps after the current price'.format(trailing_stop_step))

#remove this line to run
#sys.exit(0)

print('\nEnter \"go\" to continue. WARNING!!! CONTINUE ON YOUR OWN RISK AND ONLY IF YOU KNOW WHAT WILL HAPPEN!!!')
choice = raw_input().lower()
if choice != 'go':
    print("exit")
    sys.exit(0)


# need some sanity check.
start_price = api.getticker("BTC-" + coin)['Last']
#print('\n{}'.format(start_price))
if start_price == "INVALID_MARKET":
	print('\nThis coin pair BTC-{} is not known to bittrex'.format(coin))
	sys.exit(0)

if start_price < sl:
	print('\nYou are crasy. This will sell your coins to low. Stop Loss {:02.8f} is higher then the current price {}'.format(sl, start_price))
	sys.exit(0)

if start_price > tp:
	print('\nYou are crasy. This will sell your coins to low. Takeprofit {:02.8f} is lower then the current price {}'.format(tp, start_price))
	sys.exit(0)

i=0
while True:
    price = api.getticker("BTC-" + coin)
    last = price['Last']
    print('\n{}    {} Current Price: {:02.8f} BTC (TP={:02.8f}, SL={:02.8f})'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), coin, last, tp, sl))
    if last >= tp:
        print('\nTakeprofit reached!')
        print('Sell {:02.8f} {} for {:02.8f}'.format(quantity, coin, tp) )
        if tryrun:
            print("would sell coins")
        else:
            ret = api.selllimit('BTC-' + coin, quantity, tp)
            print(ret)
        break
    elif last <= sl:
        print('\nStop Loss taken.')
        print('Sell {:02.8f} {} for {:02.8f}'.format(quantity, coin, sl) )
        if tryrun:
            print("would sell coins")
        else:
            ret = api.selllimit('BTC-' + coin, quantity, sl)
            print(ret)
        break
    if not math.isnan(trailing_stop_start) and not math.isnan(trailing_stop_step):
        if last > trailing_stop_start:
            #print("TrailingStop aktiv")
            if last > sl + trailing_stop_step:
                print('>>TrailingStop: new stop loos reached. current price {:02.8f} BTC, old SL={:02.8f} TrailingStopSteps={:02.8f} new SL={:02.8f}'.format(last, sl, trailing_stop_step, last - trailing_stop_step))
                sl = last - trailing_stop_step
    i = i+1
    time.sleep(2)
