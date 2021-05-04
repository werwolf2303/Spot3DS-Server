import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from search import search
import subprocess
import glob

hostName = "localhost"
serverPort = 560

url = ""
first = 0


def download(url):
    subprocess.run("spotdl " + url)

def finished():
    files_in_directory = os.listdir(os.getcwd())
    filtered_files = [file for file in files_in_directory if file.endswith(".mp3")]
    for file in filtered_files:
        path_to_file = os.path.join(os.getcwd(), file)
        os.remove(path_to_file)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        url = self.path.replace("/favicon.ico", "")
        if(url.replace("/json?", "").__eq__("finish")):
            finished()
        else:
            if(url.replace("/json?", "").__contains__("search=")):
                searching = url.replace("/json?", "").replace("search=", "")
                subprocess.run("youtube-dl " + "https://www.youtube.com/watch?v=" + search(searching))
                self.wfile.write(bytes(str(glob.glob("*.mp4")).replace("['", "").replace("']", ""), "utf-8"))
                #subprocess.run("ffmpeg -i yt.mp4 -c:a libmp3lame -q:a 8 output.mp3")
            else:
                download(url)
                self.wfile.write(bytes(str(glob.glob("*.mp3")).replace("[", "").replace("'", "").replace("]", ""), "utf-8"))
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("Detected Emergency shutdown")

    webServer.server_close()
    print("Server stopped.")