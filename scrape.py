import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta

base = "https://medium.com/sitemap/posts/2019/posts-"

startDate = date(2019, 1, 1)
endDate = date.today() - timedelta(days=1)
daterange = pd.date_range(startDate, endDate)


for date in daterange:
    link = base + str(date.strftime("%Y-%m-%d")) + ".xml"
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "lxml")
    for page in soup.find_all("loc"):
      if "@" not in page:
            if 

      # filter out posts w/ '@' (comments)
      # filter out non-english posts
      # -> populate dataset, text process, create vectors 
      print(page.get_text())



