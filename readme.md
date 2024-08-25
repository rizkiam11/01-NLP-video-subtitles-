# NLP Subtitles Project

This project is focused on generating subtitles from video files using OpenAI's Whisper model. Below are the steps to set up your environment and ensure everything runs smoothly.

## Installation Guide

### 1. Install FFmpeg Locally

To process audio files, the Whisper model relies on `ffmpeg`. You need to install `ffmpeg` on your local machine. Follow the steps below based on your operating system.

#### For Windows:

1. **Download `ffmpeg`:**
   - Go to the [official FFmpeg website](https://ffmpeg.org/download.html) and download the latest version suitable for Windows.
   - Extract the contents of the zip file to a directory (e.g., `C:\ffmpeg`).

2. **Add `ffmpeg` to the System `PATH`:**
   - Right-click on `This PC` or `My Computer` and choose `Properties`.
   - Click on `Advanced system settings`.
   - Click on `Environment Variables`.
   - In the "System variables" section, find the `Path` variable and select it, then click `Edit`.
   - Click `New`, and add the path to the `ffmpeg` `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Click `OK` to close all dialogs.

3. **Verify the Installation:**
   - Open a new command prompt and type:
     ```bash
     ffmpeg -version
     ```
   - You should see the version information for `ffmpeg`, confirming it’s installed and correctly configured.

### 2. Setting Up Your Python Environment

- Clone the repository:
  ```bash
  git clone https://github.com/rizkiam11/01-NLP-video-subtitles-.git
  ```
  ```
  cd 01-NLP-video-subtitles-
  ```
- Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

-Install the required Python packages:
```
pip install -r requirements.txt
```


### 2. Running the Project
Make sure you have an audio or video file ready for processing.

1. put your video `file` in `video` directory.
2. use following command to run main file 
```
python main.py
```
3. `subtitle` folder will have the output file with `.srt`. 
