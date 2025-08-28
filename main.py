import pathlib
import pandas as pd

import whisper

from extractor.audio import extract_audio


def main():
    # TODO: need to check video path and extraction method
    # will check if the video is in local. If not, try to download from google drive.
    # If not, download from dataset.csv file

    file_path: pathlib.Path = pathlib.Path('./data/datatest.csv')
    df: pd.DataFrame = pd.read_csv(file_path)
    
    _new_row = []
    for _, row in df.iterrows():
        row_id = row['id']
        video_url = row['video']
        info = extract_audio(row_id, video_url)

        print(f'dataset_id: {row_id}: Trying to append more data')
        _new_row.append({
            "id": row_id,
            "video": video_url,
            "title": info.get('title'),
            "description": info.get("description"),
            "duration": info.get("duration"),
            "like_count": info.get("like_count"),
            "timestamp": info.get("timestamp"),
            "audio_codec": info.get("acodec"),
            "audio_bitrate": info.get("abr"),
            "audio_sampling_rate": info.get("asr"),
        })

    new_df = pd.DataFrame(_new_row)
    new_df.to_csv('./data/temp_new_df.csv')

    transcribed_audio_data = []

    audio_files = pathlib.Path('./extraction_result/audio').glob('*')
    model = whisper.load_model('small')
    # for audio in audio_files:
    #     result = model.transcribe(str(audio.absolute()))

    #     transcribed_audio_data.append({
    #         'title': audio.name,
    #         'result': result,
    #         'text': result['text']
    #     })

    audio = next(audio_files)

    print(f"Try to transcribe audio {audio.name}")
    result = model.transcribe(str(audio.absolute()))
    print(f"Transcribing {audio.name} done!")

    transcribed_audio_data.append({
        'title': audio.name,
        'result': result,
        'text': result['text']
    })

    print(transcribed_audio_data)

if __name__ == "__main__":
    main()
