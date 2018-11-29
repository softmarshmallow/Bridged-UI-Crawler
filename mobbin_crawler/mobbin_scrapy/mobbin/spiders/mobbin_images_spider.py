# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
import warnings

from mobbin_crawler.mobbin_scrapy.mobbin.items import MobbinItem
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

        cur_index = 0
        crawl_range = {"start": 0, "end": 0}
        # Enter Detail page by clicking item
        screens_divs = self.driver.find_element_by_xpath("//div[@class='sc-gNJABI dxMWgA']")

        for screen_div in screens_divs:
            screen_div.click()



        # Crawl Data from detail view
        app_name_text = self.driver.find_element_by_xpath("//h1[@class='sc-keFjpB jMBnlD']/text()").text
        app_desc_text = self.driver.find_element_by_xpath("//h1[@class='sc-jWojfa RtCwr']/text()").text

        screenshot_img = self.driver.find_element_by_xpath("//img[@class='sc-dznXNo cHYHvz']/@src")
        meta_container = self.driver.find_element_by_xpath("//div[@class='sc-cpHetk irphtn']")
        meta_patterns = meta_container.find_elements_by_xpath("./div[1]/button")
        meta_elements = meta_container.find_elements_by_xpath("./div[2]/button")
        curr_url = self.driver.current_url



        item = MobbinItem()
        item["url"] = ""
        item["file_name"] = ""
        item["app_name"] = ""
        item["category"] = ""
        item["mobbin_patterns"] = ""
        item["mobbin_elements"] = ""
        item["image_urls"] = screenshot_img

        # Exit Detail page by clicking 'X' button
        close_detail_button = self.driver.find_element_by_xpath("//button[@class='sc-erNlkL kveGTq sc-jzJRlG hvBLru']")
        close_detail_button.click()
        sleep(0.2)



        # Infinite scrolling
        while True:

            # Control when to scroll
            scrolled = self.mobbin_handle.scroll_to_bottom()
            if scrolled:
                sleep(0.5)
            else:
                sleep(3)


if __name__ == '__main__':

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MobbinImagesSpiderSpider)
    process.start()  # the script will block here until the crawling is finished
