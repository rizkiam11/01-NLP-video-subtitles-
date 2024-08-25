def format_to_srt_timenew(start, end):
    # Convert seconds to SRT time format (HH:MM:SS,MMM)
    def seconds_to_srt_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    start_time = seconds_to_srt_time(start)
    end_time = seconds_to_srt_time(end)
    return f"{start_time} --> {end_time}"
