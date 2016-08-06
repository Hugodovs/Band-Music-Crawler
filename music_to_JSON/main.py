from utils import *

if __name__ == "__main__":
#--------------------------------------------------------------------
#Input: Urls of musics
#Output: JSON File of lyrics

    #Get musicFileName and Set JSON File of lyrics
    json_filename = "database.json"
    
    #List of urls of bands
    music_urls = get_music_urls()

    #JSON File of lyrics
    lyrics_urls = crawl_lyrics(music_urls)
    
    #OUTPUT JSON File of lyrics
    output_JSONLyrics(json_filename, lyrics_urls)
#--------------------------------------------------------------------
