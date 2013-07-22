__author__ = 'brendonjohn'


class TrademeHome():
    def __init__(self, browser):
        """
        @type browser: Browser
        """
        self.browser = browser
        self.search_bar = browser.find_by_name("searchString")[0]
        self.search_button = browser.find_by_xpath("//button[@value = 'Search']")[0]

    def set_search_type(self, search_type):
        self.browser.select("searchType", search_type)

    def set_search_text(self, text):
        self.search_bar.value = text

    def click_search(self):
        self.search_button.click()