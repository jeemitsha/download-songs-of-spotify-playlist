from __future__ import unicode_literals
import youtube_dl
import os
import youtube_link

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)
def main(name):
    SAVE_PATH = r'D:'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
        'logger': MyLogger(),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link.main(name)])

    def newest(path):
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return (max(paths, key=os.path.getctime))

    return (newest(r'D:'))
