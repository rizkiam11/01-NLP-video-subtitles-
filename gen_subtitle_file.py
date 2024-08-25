from format_to_srt_time import format_to_srt_timenew
import os

subtitle_dir = "./subtitles"


def gen_subtitle_file(resultt,vid_file):
    os.makedirs(subtitle_dir, 
                    exist_ok=True)
    output_subtitle_file = os.path.join(subtitle_dir, 
                                        os.path.splitext(os.path.basename(vid_file))[0] + ".srt")
    subtitles = ""
    for i in range(len(resultt["segments"])):
        start_time = resultt["segments"][i]['start']
        end_time = resultt["segments"][i]['end']
        text = resultt["segments"][i]['text']

        subtitles += f"{i + 1}\n"
        subtitles += f"{format_to_srt_timenew(start_time, end_time)}\n"
        subtitles += f"{text}\n\n"

    # Write to .srt file
    with open(output_subtitle_file, 'w') as file:
        file.write(subtitles)

    print("Subtitles have been written...")