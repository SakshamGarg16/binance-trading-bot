import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import sys
ORDER_TYPE_STOP_MARKET = 'STOP_MARKET' 

# Logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        try:
            self.client.ping()
            logging.info("Connected to Binance Futures Testnet.")
        except Exception as e:
            logging.error("Connection failed: %s", str(e))
            sys.exit("❌ Failed to connect to Binance Testnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )

            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )

            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=stop_price,
                    quantity=quantity,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                raise ValueError("Unsupported order type.")

            logging.info("✅ Order Placed: %s", order)
            print("✅ Order executed:", order)

        except BinanceAPIException as e:
            logging.error("Binance API Error: %s", str(e))
            print("❌ API Error:", e.message)
        except Exception as e:
            logging.error("Order Placement Failed: %s", str(e))
            print("❌ Order failed:", str(e))
