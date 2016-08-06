import tkFileDialog as filedialog

import os
import codecs
import json

from scrapy.crawler import CrawlerProcess
from spiders import LyricsSpider

def get_music_urls():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        returnList = f.readlines()
    music_urls = [item.rstrip() for item in returnList]
    return music_urls    
    
def crawl_lyrics(urls_array):
    v_spider = LyricsSpider(urls=urls_array)

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(v_spider, urls=urls_array)
    process.start()

    return v_spider.lyrics_array

def output_JSONLyrics(json_filename, lyrics_urls):
    directory = filedialog.askdirectory()
    with codecs.open(os.path.join(directory, json_filename), "w", encoding="utf-8") as fp:
        json.dump(lyrics_urls, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
