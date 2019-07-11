import requests
import cld2
import re
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import date, timedelta

def init_values():
      df = pd.DataFrame(columns=["id", "url", "headline", "tags"])
      base = "https://medium.com/sitemap/posts/2019/posts-"

      startDate = date(2019, 1, 1)
      endDate = date.today() - timedelta(days=7)
      daterange = pd.date_range(startDate, endDate)

      for dt in daterange:
            link = base + str(dt.strftime("%Y-%m-%d")) + ".xml"
            res = requests.get(link)
            soup = BeautifulSoup(res.content, "lxml")
            for page in soup.find_all("loc"):
                  if "@" not in page.get_text():
                        if inspect_language(page.get_text()):
                              dfObj = populate_dataset(page.get_text())
                              df = df.append(dfObj, ignore_index=True)

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

def populate_dataset(url):
      res = requests.get(url)
      soup = BeautifulSoup(res.content)
      # will use initial response to collect article text
      for meta_data in soup.findAll("script", attrs={"data-rh": "true", "type": "application/ld+json"}):
            meta_data = json.loads(meta_data.get_text())
            tags = list(filter(lambda x: "Tag" in x, meta_data["keywords"]))
            tags = [tag.split(":")[1] for tag in tags]
            return {"id": meta_data["articleId"], "url": url, "headline": meta_data["headline"], "tags":tags}

init_values()