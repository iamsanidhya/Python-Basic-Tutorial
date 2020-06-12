import pandas as pd
import requests
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XsjUeFuF5dg')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week)