from multiprocessing import Pool
import os
import youtube_dl
from convertToMp3 import CoverterToMp3

# Create a directory to save the videos


class DownloadVideos:
    def __init__(self, save_dir):
        self.save_dir = save_dir
        self.create_save_dir()

    def create_save_dir(self):
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def get_save_dir(self):
        return self.save_dir


links = [
    'https://youtu.be/XCQs8plhq5U'
]

save_dir = 'videos2'
options = {
    'format': 'bestaudio/best',  # only download the best audio quality
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # use ffmpeg to extract audio
        'preferredcodec': 'mp3',  # specify the codec
        'preferredquality': '320',  # specify the bitrate in kbps
    }],
    # save audio with title as filename
    'outtmpl': os.path.join(save_dir, '%(title)s_%(link)s.%(ext)s'),
    'nooverwrites': True,  # don't overwrite existing files
    # download 8 videos at the same time
    'n_downloads': 10 if len(links) > 10 else len(links),
    # display log information
    'progress_hooks': [lambda x: print(f'{x["status"]}: {x["filename"]}: {x["downloaded_bytes"]}/{x["total_bytes"]}]')],
}


def download_video(link):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])


if __name__ == '__main__':
    print("---------------------------------------------------------------")
    print("-------------------DOWNLOADING VIDEOS--------------------------")
    print("---------------------------------------------------------------")
    # Download videos
    downloader = DownloadVideos(save_dir)
    print("NUMBER OF THREADS: %s", 10 if len(links) > 10 else len(links))
    with Pool(10 if len(links) > 10 else len(links)) as p:
        p.map(download_video, links)

    print("---------------------------------------------------------------")
    print("-------------------CONVERTING TO MP3---------------------------")
    print("---------------------------------------------------------------")

    # Convert to mp3
    from_format = ".webm"
    to_format = ".mp3"
    webm_folder = os.path.join(r"C:\Users\ibrah\pythonScrips", save_dir)
    mp3_folder = os.path.join(r"C:\Users\ibrah\pythonScrips", save_dir, "mp3")
    converter = CoverterToMp3(from_format, to_format, webm_folder, mp3_folder)
    converter.convert()