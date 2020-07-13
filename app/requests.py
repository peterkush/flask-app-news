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
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_movies_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        name = news_item.get ('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')


        if name:
            news_obj = News(id , name,description,url,
                            category,language,country)
            news_results.append(news_obj)
    return news_results
