"""
CodeAlpha Internship - Task 2: Stock Portfolio Tracker
Calculates total investment value from user-entered stocks and quantities,
using a hardcoded dictionary of prices. Optionally saves the result to
a .txt or .csv file.
Concepts: dictionary, input/output, basic arithmetic, file handling.
"""

import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price:>8.2f}")
    print()


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict {symbol: quantity}."""
    portfolio = {}
    print("Enter your stocks. Type 'done' when you finish.")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Try again.")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        # If the stock was entered before, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    return portfolio


def calculate_investment(portfolio):
    """Return (rows, total) where rows = [(symbol, qty, price, value), ...]."""
    rows = []
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        rows.append((symbol, qty, price, value))
        total += value
    return rows, total


def print_summary(rows, total):
    print("\n" + "=" * 46)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>16}")
    print("-" * 46)
    for symbol, qty, price, value in rows:
        print(f"{symbol:<8}{qty:>6}{price:>12.2f}{value:>16.2f}")
    print("-" * 46)
    print(f"{'TOTAL INVESTMENT':<26}{total:>20.2f}")
    print("=" * 46)


def save_to_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 46 + "\n")
        f.write(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>16}\n")
        f.write("-" * 46 + "\n")
        for symbol, qty, price, value in rows:
            f.write(f"{symbol:<8}{qty:>6}{price:>12.2f}{value:>16.2f}\n")
        f.write("-" * 46 + "\n")
        f.write(f"Total investment: {total:.2f}\n")
    print(f"Saved to {filename}")


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Saved to {filename}")


def main():
    print("=" * 40)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 40)
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Goodbye!")
        return

    rows, total = calculate_investment(portfolio)
    print_summary(rows, total)

    choice = input("\nSave result? (txt / csv / no): ").strip().lower()
    if choice == "txt":
        save_to_txt(rows, total)
    elif choice == "csv":
        save_to_csv(rows, total)
    else:
        print("Result not saved.")


if __name__ == "__main__":
    main()
