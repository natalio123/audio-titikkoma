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
    # video_urls: list[str] = df['video'].to_list()
    
    # for index, url in enumerate(video_urls, start=1):
    #     extract_audio(index, url)
    _new_row = []
    for _, row in df.iterrows():
        row_id = row['id']
        video_url = row['video']
        info = extract_audio(row_id, video_url)

        print(f'dataset_id: {row_id}: Trying to append more data')
        _new_row.append({
            "id": row_id,
            "video": video_url,
            "title": info["title"],
            "description": info["description"],
            "duration": info["duration"],
            "like_count": info["like_count"],
            "timestamp": info["timestamp"],
            "audio_codec": info["acodec"],
            "audio_bitrate": info["abr"],
            "audio_sampling_rate": info["asr"],
        })

    new_df = pd.DataFrame(_new_row)
    new_df.to_csv('./data/temp_new_df.csv')

if __name__ == "__main__":
    main()
