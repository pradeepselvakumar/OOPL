Problem: Real-Time Cryptocurrency Price Tracker

You are tasked with creating a real-time cryptocurrency price tracking application using the Observer Pattern. Multiple users (observers) can subscribe to updates on different cryptocurrencies. Each user will be notified when the price of a chosen cryptocurrency crosses a specific threshold.
Objective:

    Users (observers) will subscribe to receive real-time updates for selected cryptocurrencies (e.g., Bitcoin, Ethereum).
    The system (subject) will fetch the live price data using an external API every 30 seconds.
    When the price crosses the user-defined threshold (either above or below a target price), the system will notify all subscribed users.

Requirements:

    Cryptocurrency Class (Subject):
        This class should fetch the real-time prices of a specific cryptocurrency (e.g., Bitcoin) and notify subscribed users when the price changes.

    User Class (Observer):
        Users can set thresholds, and when the price crosses the threshold, they will be notified (e.g., “Buy now” or “Sell now”).

    Threshold Logic:
        Each user will define a threshold (e.g., buy if the price is lower than $40,000 or sell if the price is higher than $50,000).

Example Use Case:

    Alice wants to be notified when Bitcoin drops below $40,000 (to buy).
    Bob wants to be notified when Bitcoin goes above $50,000 (to sell).

Steps:

    Fetch the real-time cryptocurrency prices every 30 seconds using a real-world API.
    Notify the users when the price crosses their threshold.

API:

    Use the CoinGecko API (which doesn't require an API key) to fetch live cryptocurrency prices.
        CoinGecko API documentation
        Endpoint for fetching real-time prices: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd

Solution Outline:

    Observer Interface (User):
        Implements the update method to react to price changes.

    Subject Class (Cryptocurrency):
        Tracks the current price of a cryptocurrency and manages the list of subscribed users.
        Fetches real-time data from the CoinGecko API.

    Price Thresholds:
        Each user will define upper and lower price thresholds. When the cryptocurrency price crosses these thresholds, the observer will be notified.


### Example Usage
```
    # Create cryptocurrency object
    bitcoin = Cryptocurrency('Bitcoin', 'bitcoin')

    # Create users with thresholds for buying and selling
    alice = ConcreteUser('Alice', buy_threshold=40000, sell_threshold=60000)
    bob = ConcreteUser('Bob', buy_threshold=45000, sell_threshold=55000)

    # Subscribe users to Bitcoin updates
    bitcoin.add_user(alice)
    bitcoin.add_user(bob)

    # Start monitoring Bitcoin price (fetch every 30 seconds)
    bitcoin.monitor_price(interval=30)
```

### Sample Output
```
> python.exe .\crypto.py
Alice received update: Bitcoin is now $68045
Alice: It's time to SELL Bitcoin!
Bob received update: Bitcoin is now $68045
Bob: It's time to SELL Bitcoin!
Alice received update: Bitcoin is now $68097
Alice: It's time to SELL Bitcoin!
Bob received update: Bitcoin is now $68097
Bob: It's time to SELL Bitcoin!
Alice received update: Bitcoin is now $68097
Alice: It's time to SELL Bitcoin!
Bob received update: Bitcoin is now $68097
Bob: It's time to SELL Bitcoin!
Alice received update: Bitcoin is now $68097
Alice: It's time to SELL Bitcoin!
Bob received update: Bitcoin is now $68097
Bob: It's time to SELL Bitcoin!
```