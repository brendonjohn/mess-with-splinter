__author__ = 'brendonjohn'
from splinter import Browser
from TrademePage import TrademeHome, TrademeResults, TrademeAuction

browser = Browser()

start_url = "http://trademe.co.nz"
browser.visit(start_url)

current_page = TrademeHome(browser)
current_page.set_search_text("redcupexpress")
current_page.set_search_type("Seller")
current_page.click_search()

current_page = TrademeResults(browser)
listings_number = current_page.count_listings()

total_views = 0

for i in range(listings_number):
    listings = TrademeResults(browser).listings
    listings[i].click()

    current_page = TrademeAuction(browser)
    page_views = current_page.get_page_views()
    total_views += page_views

    print "Views for '%s': %s" % (
        current_page.get_auction_title(),
        page_views
    )

    browser.back()

print "Total listings views: %s" % (total_views)