import yt_dlp

ydl_opts = {}

def download_video(video_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

vidCount = 1
while vidCount == 1:
    link = input("Copy & paste the URL of the YouTube video you want to download: ")
    video = link.strip()

    download_video(video)
    vidCount = int(input("Enter 1 if you want to download more videos\nEnter 0 if you are done: "))
