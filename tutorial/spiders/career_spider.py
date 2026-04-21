import scrapy

class careerSpider(scrapy.Spider):
    name = "careers"
    start_urls = [
        "https://www.python.org/jobs/",
    ]

    def parse(self, response):
        for quote in response.css("ol.list-recent-jobs li"):
            yield {
                "role": quote.css("h2.listing-company span.listing-company-name a::text").get(),
                "location": quote.css("h2.listing-company span.listing-location a::text").get(),
                "tags": quote.css("span.listing-job-type a::text").getall(),
                "date": quote.css("span.listing-posted time::text").get(),
                "category": quote.css("span.listing-company-category a::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)