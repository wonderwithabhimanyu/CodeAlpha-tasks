import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}


def main():
    portfolio = {}

    print("Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock_input = input("\nEnter stock name (or 'done' to finish): ").strip()
        if not stock_input:
            continue

        stock = stock_input.upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not available.")
            continue

        while True:
            qty_str = input(f"Enter quantity of {stock}: ")
            try:
                quantity = int(qty_str)
                if quantity < 0:
                    print("Please enter a non-negative integer for quantity.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for quantity.")

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    # Calculate total investment
    total_investment = 0
    print("\nPortfolio Summary:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock} | Quantity: {qty} | Price: ${price} | Value: ${value}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional file saving
    save = input("\nDo you want to save the result? (yes/no): ").strip().lower()

    if save in ("yes", "y"):
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                writer.writerow([stock, qty, price, price * qty])
            writer.writerow(["", "", "Total", total_investment])

        print("Portfolio saved to portfolio.csv")


if __name__ == "__main__":
    main()