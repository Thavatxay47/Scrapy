import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://bongdaplus.vn/ngoai-hang-anh/diem-nhan-man-city-6-3-mu-quy-do-dang-thuong-hon-dang-trach-3783662210.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='mobover'][1]/h1[@class='artitle']").get()
        content = response.xpath("//div[@class='details']/div[@id='postContent']/p[2]").extract_first().strip()
        day = response.xpath("//div[@class='authorbox']/div[@class='dtepub']").get()
        print('tieu de', title)
        print('content', content)
        print('day', day)