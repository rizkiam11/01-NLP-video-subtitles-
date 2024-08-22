from moviepy.editor import VideoFileClip
import os


audio_dir = "./audio/"

def gen_wav_file(vid_file):
    os.makedirs(audio_dir, 
                exist_ok=True)
    output_audio_file = os.path.join(audio_dir, 
                                     os.path.splitext(os.path.basename(vid_file))[0] + ".wav")
    # Load the video clip
    video_clip = VideoFileClip(vid_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a separate file
    audio_clip.write_audiofile(output_audio_file)

    # Close the video and audio clips
    audio_clip.close()
    video_clip.close()

    print("Audio extraction successful!")

vid_file = os.path.abspath("./video/How to stay calm when you know you'll be stressed _ Daniel Levitin.mp4")
gen_wav_file(vid_file)
