stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

stock = input("Enter stock name: ").upper()

quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity

    print("\nStock:", stock)
    print("Quantity:", quantity)
    print("Total Investment Value =", total)

else:
    print("Stock not found!")