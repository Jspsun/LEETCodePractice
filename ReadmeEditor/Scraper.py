from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Config
from selenium.webdriver.common.action_chains import ActionChains


class Scraper(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.implicitly_wait(10)
        self.login()

    def login(self):
        self.browser.get('https://leetcode.com/accounts/github/login/')

        emailField = self.browser.find_element_by_id('login_field')
        passField = self.browser.find_element_by_id('password')

        emailField.send_keys(Config.user)
        passField.send_keys(Config.password)

        submitButton = self.browser.find_element_by_css_selector('.btn.btn-primary.btn-block')
        submitButton.click()
        self.browser.get('https://leetcode.com/jspsun/')

    def getQuestionsSolved(self):
        return list(map(lambda n: int(n), self.browser.find_elements_by_css_selector('.progress-bar-success')[3].text.split('/')))

    def getStars(self):
        stars = self.browser.find_element_by_css_selector('.ranking')
        ActionChains(self.browser).move_to_element(stars)

    # incomplete
    def getRanking(self):
        return 1

    def cleanup(self):
        self.browser.close()
