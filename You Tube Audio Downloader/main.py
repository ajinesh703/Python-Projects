# YouTube Audio Downloader
# Requires: pip install pytube

from pytube import YouTube
import os

def download_audio(url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}")
        out_file = audio_stream.download(output_path=output_folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print(f"Saved as: {new_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_audio(url)
