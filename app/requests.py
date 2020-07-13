from app import app
import urllib.request,json
from .models import News , Articles

#calling the api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url

base_url  = app.config["NEWS_API_BASE_URL"]


def get_news(source):
    '''
    Function that gets json responce to our url request
    '''
    get_article_url = base_url + api_key

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        Article_results = None

        if get_article_response['results']:
            news_articles_list = get_article_response['results']
            Article_results = process_results(Article_results_list)
            return articles_results


