# -*- coding: utf-8 -*-
"""
Created on Sunday November 3 2019
@author: Thomas Rolland
INESC-ID & UZA
"""
import os
import numpy as np
import scipy.io.wavfile as wav
import math
import pyaudio
import time

# Global constants
BUFFER_SIZE = 1200 #4200
CHANNELS = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE = 44100
HOP_SIZE = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME = HOP_SIZE

if __name__ == '__main__':
    # Initiating PyAudio object
    pA = pyaudio.PyAudio()
    # Open the microphone stream
    mic = pA.open(format=FORMAT, channels=CHANNELS,
            rate=SAMPLE_RATE, input=True,
            frames_per_buffer=PERIOD_SIZE_IN_FRAME)
    # Open the headset stream
    stream = pA.open(format=FORMAT,
                            channels=1,
                            rate=SAMPLE_RATE,
                            output=True)
    volume = 0.5
    silence_frame = 10
    # Main loop
    while not False:

        samples = (np.random.random(size=8300)).astype(np.float32)
        # Send this white noize the the buffer
        stream.write(volume*samples,PERIOD_SIZE_IN_FRAME)
        # Listening the imput stream from the microphone
        input_data = mic.read(PERIOD_SIZE_IN_FRAME, exception_on_overflow=False)
        # Convert into number that vad can understand it
        data = np.frombuffer(input_data, dtype=np.float32)
        # Compute the energy of the buffer
        vad = np.sum(data**2)/len(data)
        # If the energy is above 1e5 : Speech
        if vad > 1e-4:
            # We increase the volume of the white noize when speech
            volume = 1
            silence_frame = 0
        else:
            # Otherwise lower the volume
            volume = 0.1
            silence_frame += 1
        if silence_frame < 40:
            volume = 1
        print(silence_frame)
        # Create the white noize
        #samples = (np.random.random(size=16500)).astype(np.float32)
        # Send this white noize the the buffer
        #stream.write(volume*samples)

        # Wait
        #time.sleep(PERIOD_SIZE_IN_FRAME/SAMPLE_RATE)

