import yfinance as yf

stock = yf.Ticker('AAPL')

# Not functional in 12/2023
# df = stock.quarterly_earnings
# Results in: yfinance.exceptions.YFNotImplementedError: Have not implemented fetching 'earnings' from Yahoo API


# Not functional in 12/2023
# df = stock.earnings
# Results in: yfinance.exceptions.YFNotImplementedError: Have not implemented fetching 'earnings' from Yahoo API

# Income statement (default is 3 years history, I did not find a way to receive more historic data)
df = stock.income_stmt  # stock.financials can be used as well
print(df)

# Balance sheet (default is 3 years history, I did not find a way to receive more historic data)
df = stock.balance_sheet
print(df)