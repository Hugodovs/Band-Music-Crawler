# Band-Music-Crawler
Crawler for lyrics of musics

Two programs.
--------------------------------------------------------
Folders:
    
    * band_to_music:
        INPUT: Txt file with urls of bands
        OUTPUT: Txt file with urls of musics of bands
        
    * music_to_JSON:
        INPUT: Txt file with urls of musics of bands
        OUTPUT: JSON File with the following struct
        
        item = {
            'artist': artist,
            'title': title,
            'lyrics': lyrics,
            'theme': '',
            'sentiment': '',
            'url': url
        }
--------------------------------------------------------        
How to compile:
    Execute main.py file in folder band_to_music.
    Execute main.py file in folder music_to_JSON.

** The first window that opens is for you to select the INPUT file.
** The second window that opens is for you to select the OUTPUT directory.
