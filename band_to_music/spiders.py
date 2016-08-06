from scrapy.spiders import Spider
from scrapy.selector import Selector

#---------------------------------------------------#
class BandVagalumeSpider(Spider):
    name = "bandVagalume"
    
    allowed_domains = ["vagalume.com.br"]
    band_array = []
    
    def __init__(self, *args, **kwargs):
        super(BandVagalumeSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("urls")
        
    def parse(self, response):
        sel = Selector(response)
        links = response.xpath('//ol[@class="artTops"]/li/a[*]/@href').extract()
        
        for sentence in links:
            self.band_array.append(sentence)
            
        return links
#---------------------------------------------------#
