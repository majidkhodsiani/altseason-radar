from database import create_tables, get_portfolio

def show_portfolio():
    create_tables()
    assets = get_portfolio()

    if not assets:
        return "سبد خالی است"

    message = "📊 وضعیت سبد:\n\n"

    for symbol, amount in assets:
        message += f"{symbol}: {amount}\n"

    return message


if __name__ == "__main__":
    print(show_portfolio())
