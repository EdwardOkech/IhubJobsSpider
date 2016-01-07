import scrapy
from IhubJobsSpider.items import IhubjobsspiderItem

class IhubSpider(scrapy.Spider):
    name = "ihub"
    allowed_domains = ["ihub.co.ke"]
    start_urls = [
        "https://www.ihub.co.ke/jobs/"
        # "https://www.ihub.co.ke/jobs/view"
        # will uncomment this link when implementing spider following each jobs link
        # and getting the deadline and other import metrics from the job description
    ]

    def parse(self, response):
        for i in response.xpath('//div'):
            item = IhubjobsspiderItem()
            item['job_title'] = i.xpath('h3/a/text()').extract()
            item['company'] = i.xpath('div[@class="job-company"]/a/text()').extract()
            item['location'] = i.xpath('div[@class="job-location"]/text()').extract()
            item['link'] = i.xpath('h3/a/@href').extract()
            yield item

