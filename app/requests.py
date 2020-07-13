from app import app
import urllib.request,json
from .models import News , Articles

#calling the api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url

base_url  = app.config["NEWS_API_BASE_URL"]



