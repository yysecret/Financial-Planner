def get_company(ticker, timeframe, start, end, tradeapi):
    return tradeapi.get_bars(
        ticker,
        timeframe,
        start,
        end
    ).df