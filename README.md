# Kivy Android App with GitHub Actions

This is a Python Kivy application that automatically builds an Android APK using GitHub Actions.

## Project Structure

- `main.py` - Main application code
- `buildozer.spec` - Build configuration file
- `.github/workflows/build.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies

## Local Development

1. Install Python 3.9 or later
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app locally:
   ```bash
   python main.py
   ```

## Building APK Locally

1. Install Buildozer:
   ```bash
   pip install buildozer
   ```

2. Install system dependencies (Ubuntu/Debian):
   ```bash
   sudo apt-get update
   sudo apt-get install -y \
       python3-pip \
       build-essential \
       git \
       python3 \
       python3-dev \
       ffmpeg \
       libsdl2-dev \
       libsdl2-image-dev \
       libsdl2-mixer-dev \
       libsdl2-ttf-dev \
       libportmidi-dev \
       libswscale-dev \
       libavformat-dev \
       libavcodec-dev \
       zlib1g-dev \
       libgstreamer1.0 \
       gstreamer1.0-plugins-base \
       gstreamer1.0-plugins-good
   ```

3. Build the APK:
   ```bash
   buildozer android debug
   ```

## GitHub Actions

The project is set up with GitHub Actions to automatically build the APK whenever you push to the main branch or create a pull request. The built APK will be available as an artifact in the Actions tab.

## License

This project is open source and available under the MIT License. 