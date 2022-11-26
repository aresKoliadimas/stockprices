import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_STOCK_API = "3IG8AQ3YUI2UBJV8"
MY_NEWS_API = "5c34e2fedeb14781a82c1f3aed20b806"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_STOCK_API
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": MY_NEWS_API

}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [
# new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
stocks = [value for (key, value) in stock_data['Time Series (Daily)'].items()]
yesterday_closing_stock = stocks[0]['4. close']

# Get the day before yesterday's closing stock price
day_before_yesterday_closing_stock = stocks[1]['4. close']

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
stock_difference = abs(float(yesterday_closing_stock) - float(day_before_yesterday_closing_stock))

# Work out the percentage difference in price between closing price yesterday and the day before yesterday.
percentage_difference = round(100 * stock_difference / float(day_before_yesterday_closing_stock), 3)
print(percentage_difference)

# If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
news = response.json()

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
first_3_news = news['articles'][:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
news_list = [f"Headline: {new['title']}. \nBrief: {new['description']}" for new in first_3_news]
for new in news_list:
    print(new)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
