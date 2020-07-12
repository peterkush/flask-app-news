from flask import Flask
from newsapi import NewsApiClient



app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="3ecb0d19c3c24ba6a9ae749c20178705")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


     articles = topheadlines['articles']

     desc = []

     news = []

     img = []

     for i in range(len(articles)):
         myarticles = [articles[i]]


         news.append(myarticles['title'])