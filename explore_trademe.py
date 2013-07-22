__author__ = 'brendonjohn'
from splinter import Browser

browser = Browser()

start_url = "http://trademe.co.nz"
browser.visit(start_url)

search_bar = browser.find_by_name("searchString")
search_bar[0].value = "redcupexpress"
browser.select("searchType", "Seller")
button = browser.find_by_xpath("//button[@value = 'Search']")
button.click()

listings = browser.find_by_xpath("//div[@class='listingTitle']")
listings_number = len(listings)

listings_count_sum = 0
for i in range(listings_number):

    listings = browser.find_by_xpath("//div[@class='listingTitle']")
    listings[i].find_by_xpath("./a").first.click()

    # On listing page
    listing_title = browser.find_by_id("ListingTitle_title").first.text

    counters = browser.find_by_xpath("//div[@id='DetailsFooter_PageViewsPanel']/img")
    if len(counters) > 0:
        listing_count = ""
        for counter in counters:
            listing_count += counter['alt']
        listing_count = int(listing_count)
        listings_count_sum += listing_count
    else:
        listing_count = 0

    print "Views for '%s': %s" % (listing_title,listing_count)

    browser.back()

print "Total listings views: %s" % (listings_count_sum)