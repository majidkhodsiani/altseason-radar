from database import create_tables, get_portfolio
from init_portfolio import init


create_tables()

init()

portfolio = get_portfolio()

print("Current Portfolio:")
for symbol, amount in portfolio:
    print(symbol, amount)
