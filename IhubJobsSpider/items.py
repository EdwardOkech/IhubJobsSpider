import scrapy

"""
 Item model that will hold data obtained from "http://ihub.co.ke/jobs"
"""


class IhubjobsspiderItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    link = scrapy.Field()




