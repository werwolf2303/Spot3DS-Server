from youtubesearchpython import VideosSearch

def search(text):
    videosSearch = VideosSearch(text, limit=1)
    results = str(videosSearch.result())
    splits = results.replace("[", "").replace("{", "").replace("}", "").replace("]", "").split(",")
    return splits[1].replace("'id': '", "").replace("'", "")
