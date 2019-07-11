import requests
import cld2
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import date, timedelta

base = "https://medium.com/sitemap/posts/2019/posts-"

startDate = date(2019, 1, 1)
endDate = date.today() - timedelta(days=1)
daterange = pd.date_range(startDate, endDate)

def inspect_language(url):
      article_title = url.rsplit('/', 1)[-1]
      stripped = re.sub("-\n|-|\n-", " ", article_title)
      isReliable, textBytesFound, details = cld2.detect(stripped)
      if isReliable == 0:
            return False
      if "ENGLISH" in details[0] and details[0].percent > 94:
            return True
      else:
            return False

for date in daterange:
    link = base + str(date.strftime("%Y-%m-%d")) + ".xml"
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "lxml")
    for page in soup.find_all("loc"):
      if "@" not in page.get_text():
            if inspect_language(page.get_text()):
                  print(page.get_text())
                  
 # -> populate dataset, text process, create vectors 