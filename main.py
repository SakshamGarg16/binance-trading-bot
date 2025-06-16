from basic_bot import BasicBot
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    raise EnvironmentError("Missing API_KEY or API_SECRET in .env file")

def get_user_input():
    print("\n=== Binance Futures Bot ===")
    print("Supported order types: MARKET, LIMIT, STOP_MARKET")
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type: ").upper()
    quantity = float(input("Enter quantity: "))
    
    price = None
    stop_price = None

    if order_type == 'LIMIT':
        price = float(input("Enter LIMIT price: "))
    elif order_type == 'STOP_MARKET':
        stop_price = float(input("Enter STOP price (trigger level): "))

    return symbol, side, order_type, quantity, price, stop_price

if __name__ == "__main__":

    bot = BasicBot(API_KEY, API_SECRET)

    while True:
        try:
            data = get_user_input()
            bot.place_order(*data)
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped.")
            break
