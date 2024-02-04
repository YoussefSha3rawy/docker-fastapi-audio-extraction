from model import extract_audio, transcribe_audio, save_to_file
import os
import tempfile

from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/transcribe")
def transcribe(video: UploadFile):

    # Save the uploaded video file temporarily
    video_path = os.path.join(tempfile.gettempdir(), video.filename)
    with open(video_path, "wb") as video_file:
        video_file.write(video.file.read())

    audio_filename = extract_audio(video_path)

    result = transcribe_audio(audio_filename)

    print('Transcription done')

    print(result)

    return {"answer": result}


audio_filename = extract_audio(
    "")

result = transcribe_audio(audio_filename)

print('Transcription done')

print(result)

save_to_file('transcription.txt', result['text'])
