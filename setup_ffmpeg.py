"""
Automatic FFmpeg downloader and setup
"""
import os
import sys
import zipfile
import urllib.request
from pathlib import Path


def download_ffmpeg():
    """Download and extract FFmpeg if not present"""
    ffmpeg_dir = Path("ffmpeg")
    ffmpeg_exe = ffmpeg_dir / "ffmpeg.exe"
    
    # Check if already downloaded
    if ffmpeg_exe.exists():
        print("✓ FFmpeg already downloaded")
        return True
    
    print("Downloading FFmpeg...")
    print("This is a one-time download (~80MB)")
    
    # Create ffmpeg directory
    ffmpeg_dir.mkdir(exist_ok=True)
    
    # Download URL
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = "ffmpeg_temp.zip"
    
    try:
        # Download with progress
        def show_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(downloaded * 100 / total_size, 100)
            sys.stdout.write(f"\rDownloading: {percent:.1f}%")
            sys.stdout.flush()
        
        urllib.request.urlretrieve(url, zip_path, show_progress)
        print("\n✓ Download complete")
        
        # Extract
        print("Extracting FFmpeg...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Find ffmpeg.exe and ffprobe.exe in the zip
            for file in zip_ref.namelist():
                if file.endswith('bin/ffmpeg.exe') or file.endswith('bin/ffprobe.exe'):
                    # Extract to ffmpeg folder
                    filename = os.path.basename(file)
                    source = zip_ref.open(file)
                    target = open(ffmpeg_dir / filename, "wb")
                    target.write(source.read())
                    target.close()
                    source.close()
        
        print("✓ Extraction complete")
        
        # Cleanup
        os.remove(zip_path)
        print("✓ FFmpeg setup complete!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error downloading FFmpeg: {e}")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False


if __name__ == "__main__":
    download_ffmpeg()
