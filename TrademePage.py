__author__ = 'brendonjohn'


class TrademeBase(object):
    def __init__(self, browser):
        self.browser = browser


class TrademeHome(TrademeBase):
    def __init__(self, browser):
        super(TrademeHome, self).__init__(browser)

        self.search_bar = browser.find_by_name("searchString")[0]
        self.search_button = browser.find_by_xpath("//button[@value = 'Search']")[0]

    def set_search_type(self, search_type):
        self.browser.select("searchType", search_type)

    def set_search_text(self, text):
        self.search_bar.value = text

    def click_search(self):
        self.search_button.click()


class TrademeResults(TrademeBase):
    def __init__(self, browser):
        super(TrademeResults, self).__init__(browser)
        self.listings = browser.find_by_xpath("//div[@class='listingTitle']/a[1]")

    def count_listings(self):
        return len(self.listings)


class TrademeAuction(TrademeBase):
    def __init__(self, browser):
        super(TrademeAuction, self).__init__(browser)

        self.counters = browser.find_by_xpath("//div[@id='DetailsFooter_PageViewsPanel']/img")

    def get_page_views(self):
        listing_count = ""

        for counter in self.counters:
            listing_count += counter['alt']

        return int(listing_count) if len(self.counters) > 0 else 0

    def get_auction_title(self):
        return self.browser.find_by_id("ListingTitle_title").first.text