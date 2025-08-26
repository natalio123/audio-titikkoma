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
    
    # Should consider to use generator instead
    video_urls: list[str] = df['video'].to_list()
    
    # for url in video_urls:
    #     extract_audio(url)

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
