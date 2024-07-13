# Extract MP3 from MP4 Video with FFmpeg in Python 🎵

# Easily extract audio from a video file using FFmpeg with Python!

# First, install the necessary module:
# pip install ffmpeg-python

import ffmpeg

input_file = "F:\Jeh Dhamne Pamine Prani... ｜｜ જેહ ધામને પામીને પ્રાણી... ｜｜ ChosathPadi.webm"
output_file = 'output.mp3'

# Extract audio from the video
ffmpeg.input(input_file).output(output_file, format='mp3').run()

print('Audio extracted successfully!')
