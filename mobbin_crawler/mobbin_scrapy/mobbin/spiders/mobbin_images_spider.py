# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
import warnings

from mobbin_crawler.mobbin_scrapy.mobbin_handler import MobbinHandle


class MobbinImagesSpiderSpider(scrapy.Spider):
    name = 'mobbin_images_spider'
    allowed_domains = ['mobbin.design']
    start_urls = ['https://mobbin.design/patterns']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()
        self.mobbin_handle = MobbinHandle(self.driver)
        self.mobbin_handle.auto_login()

    def parse(self, response):
        self.driver.get(response.url)

        sleep(5)
        while True:
            try:
                bottom_loading_indicator = self.driver.find_element_by_xpath(
                    "//div[@class='sc-jKmXuR fiuBLV']")
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           bottom_loading_indicator)
                sleep(0.5)

            except Exception as e:
                warnings.warn(e)
                sleep(3)

        input("")


if __name__ == '__main__':

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MobbinImagesSpiderSpider)
    process.start()  # the script will block here until the crawling is finished
