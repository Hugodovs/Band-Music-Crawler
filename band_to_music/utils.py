import tkFileDialog as filedialog

import os

from scrapy.crawler import CrawlerProcess
from spiders import BandVagalumeSpider

#----------------------------------------------------------------------------------------------------#
def get_band_urls():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        returnList = f.readlines()
    band_urls = [item.rstrip() for item in returnList]
    return band_urls
    
def crawl_musics(urls_array):
    v_spider = BandVagalumeSpider(urls=urls_array)
    
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    process.crawl(v_spider, urls=urls_array)
    process.start()

    return v_spider.band_array

def output_music_urls(music_urls):
    directory = filedialog.askdirectory()
    fileopen = open(os.path.join(directory, "music_urls.txt"), "w")
    music_urls = [str(item) for item in music_urls]
    music_urls = ["https://www.vagalume.com.br{0}".format(item) for item in music_urls]
    
    for item in music_urls:
        fileopen.write(item + "\n")
        
    return music_urls
#----------------------------------------------------------------------------------------------------#
