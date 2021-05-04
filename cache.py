def createCache():
    file = open("cache.txt", "w")
    file.close()

def clearCache():
    createCache()

def readCacheALL():
    file = open("cache.txt", "r")
    return file.read()

def readCache(value):
    f = open('cache.txt', "r")
    line = f.readline()
    while line:
        line = f.readline()
        if(line.__contains__(value)):
            return line
    f.close()

def readFirstLine():
    return open("cache.txt", "r").readline()

def writeCache(text, value):
    if(readFirstLine().__eq__("")):
        file = open("cache.txt", "r")
        content = file.read()
        write = open("cache.txt", "w")
        write.write(text + ":" + value)
        write.close()
    else:
     file = open("cache.txt", "r")
     content = file.read()
     write = open("cache.txt", "w")
     write.write(content + "\n" + text + ":" + value)
     write.close()

def writeCacheEasy(value):
    if(readFirstLine().__eq__("")):
        file = open("cache.txt", "r")
        content = file.read()
        write = open("cache.txt", "w")
        write.write(value)
        write.close()
    else:
     file = open("cache.txt", "r")
     content = file.read()
     write = open("cache.txt", "w")
     write.write(content + "\n" + value)
     write.close()