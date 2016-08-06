from utils import *

if __name__ == "__main__":
#--------------------------------------------------------------------
#Input: Urls of bands
#Output: Urls of musics
       
    #List of urls of bands
    band_urls = get_band_urls()

    #List of urls of musics
    music_urls = crawl_musics(band_urls)
    
    #OUTPUT music_urls
    output_music_urls(music_urls)
#--------------------------------------------------------------------
