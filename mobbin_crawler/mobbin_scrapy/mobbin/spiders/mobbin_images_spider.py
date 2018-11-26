# -*- coding: utf-8 -*-
import scrapy
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
import warnings

USER_EMAIL = "woojoo@softmarshmallow.com"
USER_PW = "WooJoo@010104gg"

class MobbinImagesSpiderSpider(scrapy.Spider):
    name = 'mobbin_images_spider'
    allowed_domains = ['mobbin.design']
    start_urls = ['https://mobbin.design/patterns']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()
        # self.auto_login()
        self.manual_login()

    def manual_login(self):
        self.driver.get('http://mobbin.design/')
        input("press enter if login complete...")


    def auto_login(self):
        self.driver.get('http://mobbin.design/')
        login_button = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/button')
        login_button.click()
        sleep(1)
        google_login_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[1]')
        google_login_button.click()

        #     ON Google Auth page
        emailElem = self.driver.find_element_by_id('identifierId')
        emailElem.send_keys(USER_EMAIL)
        nextButton = self.driver.find_element_by_id('identifierNext')
        nextButton.click()
        sleep(1)
        passwordElem = self.driver.find_element_by_id('Passwd')
        passwordElem.send_keys(USER_PW)
        signinButton = self.driver.find_element_by_xpath('//input[@type="password"]')
        signinButton.click()


    def parse(self, response):
        self.driver.get(response.url)

        sleep(5)
        while True:
            try:
                bottom_loading_indicator = self.driver.find_element_by_xpath("//div[@class='sc-jKmXuR fiuBLV']")
                self.driver.execute_script("arguments[0].scrollIntoView();", bottom_loading_indicator)
                sleep(0.5)

            except Exception as e:
                warnings.warn(e)
                sleep(3)

        input("")



