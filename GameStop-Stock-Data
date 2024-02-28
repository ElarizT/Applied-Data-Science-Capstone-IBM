# Write important libraries
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Use Ticker function to extract data on ticker object
GameStop = yf.Ticker('GME')

# Use history function to extract stock information and use period max to take information max amount of time
gme_data = GameStop.history(period='max')

# Reset index column to make it look cleaner and show first 5 row of data using head function
gme_data.reset_index(inplace=True)
gme_data.head(5)

# Get data from the url using requests
html_data = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html')

# Use BeautifulSoup to parse html data
if html_data.status_code == 200:
    html_data = html_data.content
    soup = BeautifulSoup(html_data, 'html5lib')

# Read html data the help of pandas and io library
import io

table = soup.find_all('table')[1]

table_str = str(table)
html_io = io.StringIO(table_str)
gme_revenue = pd.read_html(html_io)[0]
gme_revenue.columns = ['Date', 'Revenue']

# Show the last 5 rows using tail function
gme_revenue.tail(5)

# Create make_graph function to visualize data
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=0.3)

    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']

    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific['Date']), y=stock_data_specific['Close'].astype("float"), name="Share Price"), row=1, col=1)

    # Convert revenue_data to numeric format by removing commas and dollar signs
    revenue_data_numeric = revenue_data_specific['Revenue'].replace('[\$,]', '', regex=True).astype(float)

    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific['Date']), y=revenue_data_numeric, name="Revenue"), row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)

    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.show()

# Assuming you have tesla_data and tesla_revenue DataFrames
make_graph(gme_data, gme_revenue, 'GameStop')
