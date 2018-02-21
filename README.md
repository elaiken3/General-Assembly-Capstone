# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) General Assembly DSI Final Capstone Project
### Eugene Aiken
### February 2018

## Project Description

Although cryptocurrency has been in existence for nearly a decade, and the concept of fiat currency currently underpins most global currencies, 2017 has been arguably the most banner year for cryptocurrencies such as Bitcoin, Ethereum and Ripple. Because this is a means of exchange that exists only in the digital space, there is quite a large online community that "discusses" news, trends, and trading strategies around this form of currency. There is no more vibrant online community than the many subreddits that exist on reddit.com. One main characteristic of late of these different cryptos is that they are EXTREMELY volatile, and can been driven up and down merely on hype. Because of this, I thought it would be interesting to see if I could identify a clear signal that would indicate an increase or decrease in the price of different cryptos based on comment thread chatter. For this particular project, I chose to use Bitcoin. There are several subreddits on reddit.com where crypto is discussed, dissected and memed at length. I chose the subreddit r/Cryptocurrency because there was a daily general discussion where people would discuss a littany of things related to the latest crypto trends.

### The Procedure:
1. Scrape Thread Comments: Reddit has an API that allows you to access their server, and some wonderful, kind soul created a Python wrapper for the Reddit API. So using a combination of the API, Python wrapper, and other web scraping techniques I scraped the top comments (origin comments), and second comments(replies to the origin comment) for a time period from September 2017 until February 2018.

2. Aggregate and process the comments: After scraping the top and second comments, I analyzed the sentiment scores of each comment using VADER Sentiment. I then grouped the scores by date and used the mean sentiment score for all the comments on a particular day. I then concatenated the data with the corresponding daily price data for Bitcoin.

3. EDA and Model Building: After I had all the data I needed cleaned and put into dataframes, I then performed EDA on the data to spot trends and correlations. Since the target (the price of Bitcoin) is time series dependent, I used an ARIMA model to analyze the data and make predictions.


## Notebook Descriptions

### Comment Collection Notebook
The Comment Collection notebook contains the code I used to scrape the comments from reddit, process the comments using VADER Sentiment Analyzer, and store them in dataframes

### Capstone EDA and Models Notebook
This notebook contains the EDA I did to gain insights about the data before building my model. It also contains the model itself and the predictions

### N-grams and Text Notebook
This notebook contains extra insights that can be derived from the actual text data itself
