import scrapy
from imspi.items import ImspiItem
from scrapy.pipelines.images import ImagesPipeline


class grgSpider(scrapy.Spider):
    name = "grg"
    allowed_domains = ["gra.m-gan.sl"]
    start_urls = ["https://gra.m-gan.sl/projects.html"]

    def parse(self, response):
        img = ImspiItem()

        relative_img_urls = response.css("img").xpath('@src').extract()
        img["image_urls"] = self.url_join(relative_img_urls, response)

        return img

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls
