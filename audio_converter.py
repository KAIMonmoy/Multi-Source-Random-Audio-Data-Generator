from glob import glob
from subprocess import call

extensions = ('m4a', 'webm')

channels = []
for ext in extensions:
    channels.extend(glob("*." + ext))

MAX_AUDIO_LEN = 10

for channel in channels:
    call(['ffmpeg', '-i', channel, "-t", str(MAX_AUDIO_LEN) + ":00",
         "channels/" + channel.split(".")[0] + ".wav"])
