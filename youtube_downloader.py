from multiprocessing import Pool
import youtube_dl
import os

# Create a directory to save the videos
save_dir = 'videos2'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


# List of YouTube links to download
links = [
    'https://youtu.be/XCQs8plhq5U',
    'https://youtu.be/utiEvVjxbtQ',
    'https://youtu.be/AAkETJn2qyA',
    'https://youtu.be/kNmUeHUR1ww',
    'https://youtu.be/eM9kGm99vKo',
    'https://youtu.be/mGOarfHJJ6o',
    'https://youtu.be/h35o7aVnd5A',
    'https://youtu.be/kqpptPkp9dY',
    'https://youtu.be/4UptgaE-g_g',
    'https://youtu.be/9NY4s82gM0Y',
    'https://youtu.be/jPJInEyz3Pc',
    'https://youtu.be/gcwCAOR0yEg',
    'https://youtu.be/tVcE5PFXpbQ',
    'https://youtu.be/vbe1ZGhGofs',
    'https://youtu.be/gt2PgbDekfc',
    'https://youtu.be/16K_2Rx4NUY',
    'https://youtu.be/S7Z9XJ1b6no',
    'https://youtu.be/gO8GFsfPe4E'
]

# Set options for youtube-dl
options = {
    'format': 'bestaudio/best',  # only download the best audio quality
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # use ffmpeg to extract audio
        'preferredcodec': 'mp3',  # specify the codec
        'preferredquality': '320',  # specify the bitrate in kbps
    }],
    # save audio with title as filename
    'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
    'nooverwrites': True,  # don't overwrite existing files
    'n_downloads': 8,  # download 8 videos at the same time
    # display log information
    'progress_hooks': [lambda x: print(f'{x["status"]}: {x["filename"]}: {x["link"]}]')],
}

# Function to download a video


def download_video(link):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])


if __name__ == '__main__':
    # Create a pool of workers to download videos in parallel
    with Pool(8) as p:
        p.map(download_video, links)
