# Stock fundamental APIs
Overview over API providers for financial fundamental data

## Python packages (free of charge)
|              | Income Statements | Balance Sheet | Ticket |
| :---         |     :---:      |     :---:     | :---: |
| yfinance     | 3 years     | 3 years      |  [Ticket for more](https://github.com/ranaroussi/yfinance/issues/1747) |
| yahoo_fin     | ...       |   ...     | ...  |



## Further APIs
|              | Finance Report History | :us: | :cn: | :india: | :kr: | :uk: | :hong_kong: | :eu: | :canada: | :jp: | Costs |
| :---         |     :---:       | :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |
| [EODHD](https://eodhd.com/r/?ref=SS55HCO7) *     | 20 years     | ✔️ | ✔️ | ✔️ | ✔️ |  ✔️ |  :x: | ✔️ | ✔️ | ✔️ | 50 EUR / month (fundamentals only) |
| [sec-api.io](https://sec-api.io)     | unlimited     ✔️  | :x: | :x: | :x: | :x: |  :x: | :x: | :x: | :x: |  after 100 free calls, 49 USD - 55 USD / month |
| [Alphavantage](https://alphavantage.co)     | 5 years    | ✔️ | :x: | :x: | :x: |  :x: | :x:  | :x: |  :x: |  free |
| [Polygon](https://polygon.io)     | up to unlimited  | ✔️ | ... | ... | ... | ... | ...  | ... |  ... |  2 years free, 5 years 29 USD, 10 years 79 USD, unlimited 199 USD |


## Stock Exchange (Ranked by trading volume of all exchanges in the country)
|              | Links |
| :---         |     :---:      |
| :us: Nasdaq | [stock list](https://www.nasdaq.com/market-activity/stocks/screener) |
| :cn: Shanghai Stock exchange (SSE) | [stock list](https://english.sse.com.cn/markets/equities/overview) |
| :india: National Stock Exchange of India (NSE India)| [stock list](https://www.nseindia.com/market-data/live-equity-market) |
| :kr: Korea Exchange (KRX) | [stock list](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0301) |
| :uk: London Stock Exchange (LSE) | [stock list](https://www.londonstockexchange.com/live-markets/market-data-dashboard/price-explorer) |
| :hong_kong: Hongkong Stock Exchange (HKEX) | [stock list](https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities?sc_lang=en)
| :eu: Euronext Exchange | [stock list](https://live.euronext.com/en/products/equities/list#)
| 🇨🇦 Toronto Stock Exchange (TSX) | [stock list](https://www.tsx.com/listings/listing-with-us/listed-company-directory)|

## Examples
EODHD: [:us:](https://eodhd.com/financial-summary/AAPL.US) [:cn:](https://eodhd.com/financial-summary/600000.SHG) [:india:](https://eodhd.com/financial-summary/TATASTEEL.NSE) [:kr:](https://eodhd.com/financial-summary/005930.KO) [:uk:](https://eodhd.com/financial-summary/SHEL.LSE)

YahooFinance [:cn:](https://finance.yahoo.com/quote/600000.SS)

Alphavantage [:us:](https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=AAPL&apikey=YOURKEY) 

Remarks:
* Affiliate link
