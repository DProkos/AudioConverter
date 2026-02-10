"""
Complete build script for Audio Converter
Downloads FFmpeg and builds standalone executable
"""
import os
import sys
import subprocess
from pathlib import Path
from setup_ffmpeg import download_ffmpeg


def install_dependencies():
    """Install required Python packages"""
    print("\n" + "="*50)
    print("Installing Python dependencies...")
    print("="*50)
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False


def build_executable():
    """Build the executable with PyInstaller"""
    print("\n" + "="*50)
    print("Building executable...")
    print("="*50)
    
    # Check if ffmpeg exists
    if not Path("ffmpeg/ffmpeg.exe").exists():
        print("✗ FFmpeg not found! Cannot build.")
        return False
    
    # Check if icon exists
    icon_path = "logo\\favicon.ico"
    if not Path(icon_path).exists():
        print(f"⚠ Warning: Icon not found at {icon_path}")
        icon_arg = "--icon=NONE"
    else:
        print(f"✓ Icon found: {icon_path}")
        icon_arg = f"--icon={icon_path}"
    
    # Clean previous builds
    print("Cleaning previous builds...")
    for folder in ["build", "dist"]:
        if Path(folder).exists():
            import shutil
            shutil.rmtree(folder)
    
    if Path("AudioConverter.spec").exists():
        os.remove("AudioConverter.spec")
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "AudioConverter",
        "--add-data", "ffmpeg;ffmpeg",
        "--add-data", "logo;logo",
        icon_arg,
        "audio_converter.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "="*50)
        print("✓ Build complete!")
        print("="*50)
        print("\nYour executable is at: dist\\AudioConverter.exe")
        print("\nThe .exe is fully standalone and includes:")
        print("  - PyQt5 GUI")
        print("  - pydub audio processing")
        print("  - FFmpeg (embedded)")
        print("  - Custom icon")
        print("\nYou can distribute AudioConverter.exe without any dependencies!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        return False


def main():
    print("="*50)
    print("Audio Converter - Complete Build Script")
    print("="*50)
    
    # Step 1: Download FFmpeg
    print("\n[Step 1/3] Checking FFmpeg...")
    if not download_ffmpeg():
        print("✗ Failed to setup FFmpeg")
        return
    
    # Step 2: Install dependencies
    print("\n[Step 2/3] Installing dependencies...")
    if not install_dependencies():
        print("✗ Failed to install dependencies")
        return
    
    # Step 3: Build executable
    print("\n[Step 3/3] Building executable...")
    if not build_executable():
        print("✗ Build failed")
        return
    
    print("\n" + "="*50)
    print("All done! 🎉")
    print("="*50)


if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
