import pathlib
import pandas as pd

import yt_dlp

def extract_video(url: str):
    pass

def main():
    # TODO: need to check video path and extraction method
    # will check if the video is in local. If not, try to download from google drive.
    # If not, download from dataset.csv file

    file_path: pathlib.Path = pathlib.Path('./data/datatest.csv')
    df: pd.DataFrame = pd.read_csv(file_path)
    
    # Should consider to use generator instead
    video_urls: list[str] = df['video'].to_list()
    
    for url in video_urls:
        ytdlp_ops = {
            'extract_flat': 'discard_in_playlist',
            'format': 'bestaudio/best', # comment this to get noth audio and video
            'fragment_retries': 10,
            'ignoreerrors': 'only_download',
            'max_sleep_interval': 100.0,
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                                'nopostoverwrites': False,
                                'preferredcodec': 'best',
                                'preferredquality': '5'},
                                {'key': 'FFmpegConcat',
                                'only_multi_video': True,
                                'when': 'playlist'}],
            'retries': 10,
            'sleep_interval': 60.0,
            'verbose': True,
            'warn_when_outdated': True,
            'paths': {
                'home': './extraction_result/audio'
            },
        }
        with yt_dlp.YoutubeDL(ytdlp_ops) as ydl:
            info = ydl.extract_info(url) 
            sanitized_info = ydl.sanitize_info(info)
            print(sanitized_info)


if __name__ == "__main__":
    main()
