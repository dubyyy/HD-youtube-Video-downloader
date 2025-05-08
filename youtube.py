import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',  # Ensures high-quality video+audio merging
        'merge_output_format': 'mp4',  # Ensures merged output in MP4 format
        'outtmpl': '%(title)s.%(ext)s',  # Save with video title as filename
        'quiet': False,  # Show download progress
        'postprocessors': [{  
            'key': 'FFmpegVideoConvertor',  
            'preferedformat': 'mp4'  # Convert to MP4 if needed
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
    print("Download complete!")
#https://www.youtube.com/watch?v=qyfBj44Bykc