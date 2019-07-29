import pandas as pd

def main(input):
  db = pd.read_csv('medium_data.csv')
  article = db[db['headline'] == input]
  canidates = get_similar(article, db)

def get_similar(article, db):
  tags = article.tags
  canidates = db.tags.isin(tags)
