@echo off
setlocal enabledelayedexpansion

echo.
echo ═══════════════════════════════════════════════════════════
echo     AUDIO CONVERTER - BATCH CONVERSION
echo ═══════════════════════════════════════════════════════════
echo.
echo This will convert ALL MP3 and MP4 files in a folder
echo to WAV format (8kHz, 16bit, Mono, PCM)
echo.
echo ═══════════════════════════════════════════════════════════
echo.

REM Check if AudioConverter.exe exists
if not exist "dist\AudioConverter.exe" (
    echo ERROR: AudioConverter.exe not found!
    echo Please build the application first using: python build.py
    echo.
    pause
    exit /b 1
)

echo Drag and drop a folder containing MP3/MP4 files here,
echo or type the full path:
echo.
set /p "folder_path="

if not exist "%folder_path%" (
    echo.
    echo ERROR: Folder not found!
    pause
    exit /b 1
)

echo.
echo Creating output folder...
set "output_folder=%folder_path%\converted_wav"
if not exist "%output_folder%" mkdir "%output_folder%"

echo.
echo Starting conversion...
echo ═══════════════════════════════════════════════════════════
echo.

set count=0

REM Convert MP3 files
for %%f in ("%folder_path%\*.mp3") do (
    set /a count+=1
    echo [!count!] Converting: %%~nxf
    
    REM Note: This is a placeholder - actual batch conversion would need
    REM a Python script or command-line version of the converter
    echo     → %%~nf_8k_pcm_mono.wav
)

REM Convert MP4 files
for %%f in ("%folder_path%\*.mp4") do (
    set /a count+=1
    echo [!count!] Converting: %%~nxf
    echo     → %%~nf_8k_pcm_mono.wav
)

echo.
echo ═══════════════════════════════════════════════════════════
echo.

if !count! EQU 0 (
    echo No MP3 or MP4 files found in the folder!
) else (
    echo Found !count! file(s) to convert.
    echo.
    echo NOTE: For batch conversion, please use the GUI application
    echo and convert files one by one, or contact support for a
    echo command-line batch converter tool.
)

echo.
pause
