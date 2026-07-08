from database import create_tables, add_asset

portfolio = {
    "ENA": 80000,
    "XRP": 5500,
    "FIL": 9000,
    "ENS": 5000,
    "ENJ": 51000,
    "X": 65000000,
    "PENGU": 52000,
    "SHIB": 800000000,
    "MAGIC": 36500,
    "POL": 28000,
    "SUI": 200,
    "TRX": 43,
    "DOGE": 16000
}


def init():
    create_tables()

    for symbol, amount in portfolio.items():
        add_asset(symbol, amount)

    print("Portfolio initialized successfully")


if __name__ == "__main__":
    init()
