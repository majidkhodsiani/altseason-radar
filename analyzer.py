def analyze_coin(symbol):
    return {
        "symbol": symbol,
        "rsi": None,
        "macd": None,
        "divergence": "unknown",
        "decision": "waiting"
    }


def analyze_portfolio(portfolio):

    results = []

    for coin in portfolio:
        results.append(
            analyze_coin(coin)
        )

    return results
