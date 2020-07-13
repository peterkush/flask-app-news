class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,description,url,language,country):
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.category = category
        self.country = country

class Articles:
    '''
    Articles class to Articles Objects
    '''
    def __init__(self, author,tittle, description,url, urlToImage,publishedAt, content):
        self.author = author
        self.title = tittle
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt
        self.content = content
        