# 🤖 Binance Futures Trading Bot (Python)

A simplified command-line trading bot for the Binance **USDT-M Futures Testnet**, built in Python using the `python-binance` library.

This project is part of the technical assignment for the **Junior Python Developer** role at **PrimeTrade.ai**.

---

## ✨ Features

- ✅ Place **Market**, **Limit**, and **Stop-Market** orders  
- ✅ Supports **Buy** and **Sell** sides  
- ✅ Built using official Binance Futures Testnet API  
- ✅ Secure API key handling using `.env`  
- ✅ Full logging of API actions and errors (`bot.log`)  
- ✅ Input validation and error messages via CLI  
- ✅ Structured for easy future extensions (e.g., Grid, OCO, TWAP)

---

## 📁 Project Structure
binance-trading-bot/
├── main.py # CLI interface to place orders
├── basic_bot.py # Core bot logic for order handling
├── requirements.txt # Python dependencies
├── bot.log # Log file auto-generated on execution
├── README.md # Project documentation
└── .env # Stores Binance API credentials (ignored by Git)


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
```

### 2. Clone the repository

```bash
pip install -r requirements.txt
```

### 3. Clone the repository

```bash
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret

```

### 4. Run the bot

```bash
python main.py
```

### 💬 Example CLI Usage
```yaml
=== Binance Futures Bot ===
Supported order types: MARKET, LIMIT, STOP_MARKET

Enter symbol (e.g., BTCUSDT): BTCUSDT
Enter side (BUY or SELL): BUY
Enter order type: LIMIT
Enter quantity: 0.01
Enter LIMIT price: 57000

✅ Order executed: {'orderId': 12345, 'status': 'NEW', ...}
```
### Log File (bot.log)
All API requests, responses, and errors are logged with timestamps.

Example:
```yaml
2025-06-14 22:10:44,343 - INFO - ✅ Order Placed: {'symbol': 'BTCUSDT', 'side': 'BUY', ...}
2025-06-14 22:11:01,457 - ERROR - Binance API Error: Insufficient margin
```

## 📦 Requirements

- Python 3.8+
- Binance API credentials (Testnet)  
  👉 [Create Binance Futures Testnet account](https://testnet.binancefuture.com)
- Internet connection
- Python packages:
  - `python-binance`
  - `python-dotenv`

### Install via pip

```bash
pip install python-binance python-dotenv
```


## 🧠 Potential Improvements

- Integrate **WebSockets** for real-time price updates  
- Build a **basic dashboard** for trade status and order tracking  
- Add **portfolio tracking** and real-time **P&L reporting**

---

## 👤 Author

**Saksham Garg**  
📧 gargsaksham16@gmail.com  


---

## 🛑 Disclaimer

This bot runs on the **Binance Futures Testnet**. It is for **demonstration and educational purposes only**.  
Do **not** use this bot for live trading or with real funds without appropriate risk management.


