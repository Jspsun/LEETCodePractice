from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Config
from selenium.webdriver.common.action_chains import ActionChains

import time
import datetime
import os.path

class Scraper:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)

        self.browser.get('https://leetcode.com/accounts/github/login/')

        emailField = self.browser.find_element_by_id('login_field')
        passField = self.browser.find_element_by_id('password')

        emailField.send_keys(Config.user)
        passField.send_keys(Config.password)

        submitButton = self.browser.find_element_by_css_selector('.btn.btn-primary.btn-block')
        submitButton.click()
        self.browser.get('https://leetcode.com/jspsun/')

    def getQuestionsSolved(self):
        return self.browser.find_elements_by_css_selector('.progress-bar-success')[3].text

    def getRank(self):
        stars = self.browser.find_element_by_css_selector('.ranking')
        ActionChains(self.browser).move_to_element(stars)

    def getStars(self):
        return 1

    def cleanup(self):
        self.browser.close()
#----------------------------------------------------------------------------------

# class Printer:

#     def __init__(self):
#         self.


#----------------------------------------------------------------------------------
if __name__ == "__main__":
    S = Scraper()
    print S.getQuestionsSolved()
    print S.getRank()
    S.cleanup()
