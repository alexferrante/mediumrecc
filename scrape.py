import requests
import cld2
import re
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import date, timedelta

def init_values():
      df = pd.DataFrame(columns=["id", "url", "headline", "tags", "content"])
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
                        article_title = page.get_text().rsplit('/', 1)[-1]
                        stripped = re.sub("-\n|-|\n-", " ", article_title)
                        if inspect_language(article_title):
                              dfObj = populate_dataset(page.get_text())
                              df = df.append(dfObj, ignore_index=True)
      df.to_csv('medium_dataset', sep='\t')

def inspect_language(text):
      isReliable, textBytesFound, details = cld2.detect(text)
      if isReliable == 0:
            return False
      if "ENGLISH" in details[0] and details[0].percent > 94:
            return True
      else:
            return False

def populate_dataset(url):
      print("Populating dataset with ", url, "...")
      res = requests.get(url)
      soup = BeautifulSoup(res.content)
      #article_content = soup.find("article").get_text() article content can be accessed here
      for meta_data in soup.findAll("script", attrs={"data-rh": "true", "type": "application/ld+json"}):
            print("Collecting article metadata...")
            meta_data = json.loads(meta_data.get_text())
            tags = list(filter(lambda x: "Tag" in x, meta_data["keywords"]))
            tags = [tag.split(":")[1] for tag in tags]
            if inspect_language(" ".join(str(x) for x in tags)) is False:
                  continue
            return {"id": meta_data["articleId"], "url": url, "headline": meta_data["headline"], "tags":tags}

init_values()
