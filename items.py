import scrapy

class NewsItem(scrapy.Item):
    # news article attributes defined below:
    title = scrapy.Field()
    authors = scrapy.Field()
    url = scrapy.Field()
    paragraphs = scrapy.Field()
    #images = scrapy.Field()
    #comments = scrapy.Field()
    #date = scrapy.Field()

    # pass
