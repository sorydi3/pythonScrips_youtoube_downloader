from multiprocessing import Pool
import youtube_dl
import os

# Create a directory to save the videos


class DownloadVideos:
    def __init__(self, links, save_dir):
        self.links = links
        self.save_dir = save_dir
        self.options = None
        self.create_save_dir()

    def create_save_dir(self):
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def download_video(self, link):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([link])

    def get_save_dir(self):
        return self.save_dir

    def set_options(self, options):
        self.options = options

    def download_videos(self):
        # Create a pool of workers to download videos in parallel
        print("Downloading videos... pools %s", self.links)
        with Pool(8) as p:
            p.map(self.links)

    def run(self):
        self.download_videos()


if __name__ == '__main__':
    # Download videos
    save_dir = 'videos_test'
    links = [
        'https://youtu.be/XCQs8plhq5U',
        'https://youtu.be/S7Z9XJ1b6no',
        'https://youtu.be/gO8GFsfPe4E'
    ]

    downloader = DownloadVideos(links, save_dir)
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
        'n_downloads': 8,  # download 8 videos at the same time
        # display log information
        'progress_hooks': [lambda x: print(f'{x["status"]}: {x["filename"]}: {x["downloaded_bytes"]}/{x["total_bytes"]}]')],
    }

    downloader.set_options(options)
    print("Downloading videos...")

    with Pool(8) as p:
        p.map(downloader.download_video, links)

    # downloader.run()

    # Convert to mp3
