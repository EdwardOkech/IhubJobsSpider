import scrapy


class IhubjobsspiderItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    link = scrapy.Field()




