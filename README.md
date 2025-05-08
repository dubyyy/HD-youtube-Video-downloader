YouTube Video Downloader (MP4)
A simple Python script to download YouTube videos in high-quality MP4 format using yt_dlp.

Features
Downloads the best available video and audio, then merges them.

Ensures the output is in .mp4 format.

Uses video title as the filename.

Displays download progress in the terminal.

Requirements
Python 3.7+

yt_dlp

ffmpeg (for merging video and audio)

Installation
Clone this repository or copy the script file:

bash
Copy
Edit
git clone https://github.com/yourusername/yt-video-downloader.git
cd yt-video-downloader
Install dependencies:

bash
Copy
Edit
pip install yt-dlp
Install ffmpeg (if not already installed):

macOS: brew install ffmpeg

Windows: Download from ffmpeg.org and add to your PATH

Linux: sudo apt install ffmpeg

Usage
Run the script from your terminal:

bash
Copy
Edit
python download_video.py
Then enter the YouTube video URL when prompted.

Example:

less
Copy
Edit
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Download complete!
The downloaded .mp4 file will be saved in the current directory with the video's title as the filename.

License
This project is licensed under the MIT License
