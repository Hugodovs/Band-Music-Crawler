import re

from scrapy.spiders import Spider
from scrapy.selector import Selector

#---------------------------------------------------#
class LyricsSpider(Spider):
    name = "vagalume"

    allowed_domains = ["vagalume.com.br"]
    lyrics_array = []

    def __init__(self, *args, **kwargs):
        super(LyricsSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('urls')

    def parse(self, response):
        sel = Selector(response)

        artist_path = sel.xpath('//*[@id="header"]/p[1]/a/text()')[0]
        artist = artist_path.extract()

        title_path = sel.xpath('//*[@id="header"]/h1/text()')[0]
        title = title_path.extract()
        title = title.strip()

        lyrics_path = sel.xpath('//*[@id="lyr_original"]/div')[0]
        lyrics = lyrics_path.extract()

        lyrics = lyrics.replace("<br>", "\n")
        lyrics = re.sub('<.*?>', '', lyrics)
        lyrics = lyrics.strip()

        item = {
            'artist': artist,
            'title': title,
            'lyrics': lyrics,
            'theme': '',
            'sentiment': '',
            'url': response.url
        }

        self.lyrics_array.append(item)
        return lyrics
#---------------------------------------------------#
