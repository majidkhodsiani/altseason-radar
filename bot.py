import json

PORTFOLIO_FILE = "portfolio.json"


def load_portfolio():
    with open(PORTFOLIO_FILE, "r") as file:
        return json.load(file)


def show_portfolio():
    portfolio = load_portfolio()

    text = "📊 سبد فعلی:\n\n"

    for coin, amount in portfolio.items():
        text += f"{coin}: {amount}\n"

    return text


if __name__ == "__main__":
    print(show_portfolio())
