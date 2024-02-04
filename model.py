from transformers import pipeline
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip

asr_pipeline = pipeline("automatic-speech-recognition",
                        model="openai/whisper-small", device='mps')


def extract_audio(video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_filename = f'extracted_audio.wav'
    audio_clip.write_audiofile(audio_filename)
    audio_clip.close()
    video_clip.close()
    return audio_filename


def transcribe_audio(audio_path):
    print('Transcribing audio...')
    result = asr_pipeline(audio_path)
    return result


def save_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
