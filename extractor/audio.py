import yt_dlp

def extract_audio(id: int, url: str):
    ytdlp_ops = {
        'extract_flat': 'discard_in_playlist',
        'format': 'bestaudio/best', # comment this to get both audio and video
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
            'home': './extraction_result/audio' # TODO: use constant or config instead of hardcoding
        },
        'outtmpl': {
            'default': f'{id}_%(title)s [%(id)s].%(ext)s'},
    }

    with yt_dlp.YoutubeDL(ytdlp_ops) as ydl:
        info = ydl.extract_info(url) 
        if info:
            return info
        return {}
