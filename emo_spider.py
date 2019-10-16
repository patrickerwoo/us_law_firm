import scrapy
from emojispider.items import EmojiSpiderItem

class EmoSpider(scrapy.Spider):
    name = 'emo'
    allowed_domains = ['emoji-cheat-sheet.com']
    start_urls = [
    'https://www.martindale.com',
    ]

def parse(self, response):
    self.log('A response from %s just arrived!' % response.url)