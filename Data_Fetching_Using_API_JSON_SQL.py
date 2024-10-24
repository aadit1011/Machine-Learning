# Import necessary libraries for API requests and data manipulation
import requests as rq
import pandas as pd
import mysql.connector as sq

# ----------- API Example 1: Random User API -------------
# API link: https://randomuser.me/
# Fetch random user data and load it into a pandas DataFrame

response = rq.get('https://randomuser.me/api')  # Make the GET request to Random User API
result = response.json()['results']  # Parse the JSON response and extract results
df_user = pd.DataFrame(result)  # Convert the result into a DataFrame
print("Random User Data:")
print(df_user)

# ----------- API Example 2: OpenWeatherMap API -------------
# API link: https://home.openweathermap.org/
# Fetch current weather data for a specific city

API_KEY = 'your_api_key'  # Replace with your OpenWeatherMap API key
city = 'London'  # Change the city as needed
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'  # API request URL
response = rq.get(url)  # Make the GET request to OpenWeatherMap API
weather_data = response.json()['weather']  # Extract weather information
df_weather = pd.DataFrame(weather_data)  # Convert the result into a DataFrame
print("\nCurrent Weather Data:")
print(df_weather)

# ----------- API Example 3: Alpha Vantage API -------------
# API link: https://www.alphavantage.co/
# Fetch daily time series stock data for a given stock symbol

API_KEY = 'your_api_key'  # Replace with your Alpha Vantage API key
symbol = 'AAPL'  # Change the stock symbol if needed
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'  # API request URL
response = rq.get(url)  # Make the GET request to Alpha Vantage API
stock_data = response.json()  # Parse the JSON response
df_stock = pd.DataFrame(stock_data['Time Series (Daily)'])  # Extract the daily time series data into a DataFrame
print("\nStock Data for AAPL:")
print(df_stock.head())

# ----------- API Example 4: NASA API -------------
# API link: https://api.nasa.gov/
# Fetch NASA Astronomy Picture of the Day (APOD)

API_KEY = 'your_api_key'  # Replace with your NASA API key
url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'  # API request URL
response = rq.get(url)  # Make the GET request to NASA API
nasa_data = response.json()  # Parse the JSON response
df_nasa = pd.DataFrame([nasa_data])  # Load the data into a DataFrame
print("\nNASA Astronomy Picture of the Day:")
print(df_nasa.head())

# ----------- Loading JSON data into a pandas DataFrame -------------
# If you have a local JSON file (e.g., 'test.json'), you can load it using pd.read_json()

df_json = pd.read_json('test.json')  # Replace 'test.json' with the actual file path
print("\nData from JSON file:")
print(df_json)

# ----------- MySQL Database Connection Example -------------
# Establish a connection to a local MySQL database and load tables into pandas DataFrames

# Connect to the MySQL database using MySQL Connector
con = sq.connect(host='localhost', user='root', password='', database='world')  # Ensure that MySQL is running

# Fetch city, country, and country language tables from the MySQL database
city = pd.read_sql_query('SELECT * FROM city', con)
country = pd.read_sql_query('SELECT * FROM country', con)
country_language = pd.read_sql_query('SELECT * FROM countrylanguage', con)

# Display the first few records from each table
print("\nCity Data:")
print(city.head())

print("\nCountry Data:")
print(country.head())

print("\nCountry Language Data:")
print(country_language.head())

# ----------- Query: Filter countries with Life Expectancy greater than 50 -------------
# Apply a filter to the country DataFrame to get countries with LifeExpectancy > 50

high_life_expectancy = country[country['LifeExpectancy'] > 50]
print("\nCountries with Life Expectancy > 50:")
print(high_life_expectancy)

# Close the MySQL connection
con.close()
