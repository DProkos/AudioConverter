@echo off
echo Cleaning temporary build files...
echo.

if exist "__pycache__" (
    rmdir /s /q __pycache__
    echo ✓ Removed __pycache__
)

if exist "build" (
    rmdir /s /q build
    echo ✓ Removed build
)

if exist "*.spec" (
    del /q *.spec
    echo ✓ Removed .spec files
)

echo.
echo ✓ Cleanup complete!
pause
