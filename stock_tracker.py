stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_value = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT) or 'done': ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_value += investment
    else:
        print("Stock not found!")

print("Total Investment Value = $", total_value)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total_value))
file.close()

print("Result saved in portfolio.txt")
