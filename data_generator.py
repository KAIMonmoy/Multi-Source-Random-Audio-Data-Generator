import numpy as np
import pandas as pd

from subprocess import call

MAX_AUDIO_LEN = 10

for idx in range(7):
    len_so_far = 0
    durations = []
    channels = []
    while len_so_far < MAX_AUDIO_LEN:
        cur_len = np.random.randint(1, 3)
        if len_so_far + cur_len > 10:
            cur_len = 10 - len_so_far
        durations.append((len_so_far, cur_len))
        len_so_far += cur_len
        cur_channel = np.random.randint(1, 6)
        while len(channels) > 0 and cur_channel == channels[-1]:
            cur_channel = np.random.randint(1, 6)
        channels.append(cur_channel)

    for i, (channel, (start, dur)) in enumerate(zip(channels, durations)):
        channel_name = "channels/channel_" + str(channel) + ".wav"
        temp_name = "data/temp_" + str(i) + ".wav"
        start_time = "0" + str(start) + ":00"
        duration = "0" + str(dur) + ":00"
        call(["ffmpeg", "-loglevel", "1", "-i", channel_name,
              "-ss",      start_time, "-t", duration, temp_name])

    annotation = {
        "start_time": [str(dur[0]) + ":00" for dur in durations],
        "end_time": [str(dur[0] + dur[1]) + ":00" for dur in durations],
        "channel": channels
    }
    pd.DataFrame(data=annotation).to_csv(
        'annotations/data_' + str(idx+1) + '.csv')

    data_builder = ["sox"]
    for i in range(len(channels)):
        temp_wav = "data/temp_" + str(i) + ".wav"
        data_builder.append(temp_wav)
    data_name = "data/data_" + str(idx+1) + ".wav"
    data_builder.append(data_name)

    call(data_builder)

    data_builder.pop()
    data_builder[0] = "rm"

    call(data_builder)
