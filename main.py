import pathlib
import pandas as pd
from extractor.audio import extract_audio

def main():
    # TODO: need to check video path and extraction method
    # will check if the video is in local. If not, try to download from google drive.
    # If not, download from dataset.csv file

    file_path: pathlib.Path = pathlib.Path('./data/datatest.csv')
    df: pd.DataFrame = pd.read_csv(file_path)
    
    # Should consider to use generator instead
    video_urls: list[str] = df['video'].to_list()
    
    for url in video_urls:
        extract_audio(url)

if __name__ == "__main__":
    main()
