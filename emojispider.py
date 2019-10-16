import scrapy

class EmojiSpiderItem(scrapy.item):
    emoji_handle = scrapy.Field()
    emoji_image = scrapy.Field()
    section = scrapy.Field()

