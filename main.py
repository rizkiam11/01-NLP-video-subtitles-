import whisper
import numpy as np
from extract_audio_from_video import gen_wav_file



# model = whisper.load_model("base")
print(whisper.available_models())
# model = whisper.load_model("base", download_root= "./models")
model= whisper.load_model("./models/base.pt")
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)

gen_wav_file("./video/How to stay calm when you know you'll be stressed _ Daniel Levitin.mp4")

# import torch
# print(torch.__version__)
# print(torch.cuda.is_available())
