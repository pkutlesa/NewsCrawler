import scrapy
from news.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = "news"

    def start_requests(self):
        urls = [
            'https://www.nytimes.com/2020/10/03/us/coronavirus-united-states.html?action=click&module=Spotlight&pgtype=Homepage',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = NewsItem()   # return item

        # article title and authors found in <header> element of response
        header = response.xpath('//header')
        item['title'] = header.xpath('.//h1[contains(@itemprop, "headline")]/text()').get()
        item['authors'] = header.xpath('.//span[contains(@itemprop, "name")]/text()').getall()

        # article body contains section paragraphs, images, etc.
        body = response.xpath('//section[contains(@name, "articleBody")]')
        # text for each paragraph <p> tag. have to merge text from nested elements as well (e.g., <a> tags)
        paragraphs = []
        for paragraph in body.xpath('.//p'):
            cumulater = ''
            for text in paragraph.xpath('.//text()').getall():
                cumulater += text
            paragraphs.append(cumulater)
        item['paragraphs'] = paragraphs

        # meta data
        item['url'] = response.url

        yield item
        # get url of next article and yield new Request to continue crawl






