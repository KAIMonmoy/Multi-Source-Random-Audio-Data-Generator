# Multi-Source Random Audio Data Generator

## Audio Download

### Requirements

- [youtuble-dl](https://github.com/ytdl-org/youtube-dl)

### Code

```sh
 youtube-dl -f 'bestaudio' -o 'channel_<CHANNEL_NO>.%(ext)s' <VIDEO_URL>
```

### Example Channel List

- Channel 1 : https://www.youtube.com/watch\?v\=xAiA4ubcGjA
- Channel 2 : https://www.youtube.com/watch\?v\=hobgFoZ899I
- Channel 3 : https://www.youtube.com/watch\?v\=1pXVxJrKP1w
- Channel 4 : https://www.youtube.com/watch\?v\=qijNijvUbdA
- Channel 5 : https://www.youtube.com/watch\?v\=CIMyEoYZfio

## Audio Crop and Conversion

### Requirements

- python 3
- ffmpeg
- sox

### Code

- [Audio Cropper Converter Python Script](audio_converter.py)

- ```sh
    # Audio Re-sampling
    sox <INPUT_FILE> -r <SAMPLING_RATE> <OUTPUT_FILE>
  ```

## Audio Data Generator

### Requirements

- python 3
- numpy
- pandas
- ffmpeg
- sox

### Code

- [Audio Data Generator Python Script](data_generator.py)
