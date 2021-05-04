from youtubesearchpython import VideosSearch
from cache import *

def search(text):
    videosSearch = VideosSearch(text, limit=1)
    results = str(videosSearch.result())
    splits = results.replace("[", "").replace("{", "").replace("}", "").replace("]", "").split(",")
    writeCacheEasy(splits[1].replace("'id': '", "").replace("'", ""))
    return splits[1].replace("'id': '", "").replace("'", "")
