import whisper
import numpy as np
from extract_audio_from_video import gen_wav_file
from gen_subtitle_file import gen_subtitle_file
import os
import time
import librosa

# def seconds_to_minutes_and_seconds(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     return int(minutes), int(seconds)

# seconds_to_minutes_and_seconds(librosa.get_duration(path = audio))

# ******to view all available models.
# print(whisper.available_models())


#download and load the base model
model = whisper.load_model("base")

#*****to download and load model file in directory. to avoid downloading of model for every run*****
# model = whisper.load_model("base", download_root= "./models")
# model = whisper.load_model("./models/base.pt")

# details of model
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)

video_dir = "./video"
video_file_name = os.listdir("./video")[0]
video_file_path = "/".join(["./video",video_file_name])

if not os.path.exists(video_file_path):
    print("video File not found:")
print(video_file_path)


gen_wav_file(video_file_path)


file_name = os.listdir("./audio")[0]
audio_file_path = "/".join(["./audio",file_name])

if not os.path.exists(audio_file_path):
    print("File not found:", audio_file_path)
else:
    audio_duration = librosa.get_duration(path = audio_file_path)
    audio_minutes, audio_seconds = divmod(audio_duration, 60)
    print("transcribe started")
    # Start time
    start_time = time.time()
    result = model.transcribe(audio_file_path)
    # End time
    end_time = time.time()
    # Calculate the execution time
    execution_time = end_time - start_time
    minutes, seconds = divmod(execution_time, 60)
    print(f"transcribe succesfully {int(audio_minutes)}:{int(audio_seconds)} audio file in {int(minutes)}:{int(seconds)}")

# print(audio_file_path)
# print(result)
                                                                                                                                                                                                                                  
if result is not None:
    print("Subtitle creation started")
<<<<<<< HEAD
    gen_subtitle_file(result,video_file_path)
=======
    gen_subtitle_file(result,video_file_path)
>>>>>>> e496267cc3573bce49b7ce33f0dc9faa53c766ed
