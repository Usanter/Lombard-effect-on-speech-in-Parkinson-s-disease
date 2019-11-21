import os
import numpy as np
import pyaudio
from guizero import App, PushButton, Text, Slider, Picture
# Global constants
BUFFER_SIZE = 1200 #4200
CHANNELS = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE = 44100
HOP_SIZE = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME = HOP_SIZE

class LombardTool():
    def __init__(self):
        # Variables definition
        self.volume = 0.1
        self.silence_frame = 50
        self.noise_value = 0
        self.db_value = 0
        self.state = False #  0 = Pause; 1 = play
        # ========== GUI =============
        # Create the GUI app
        self.app = App(title="Lombard effect on speech in Parkinson's disease App")
        # Energy detection option
        self.message = Text(self.app, text="Select threshold for voice detection")
        self.slider = Slider(self.app,start=0,end=6, command=self.slider_noise)
        # Noise characteristic option
        self.message2 = Text(self.app,text="Select noise in dB")
        self.slider2 = Slider(self.app,start=0,end=10,command=self.slider_db)
        # Play/pause button
        self.button = PushButton(self.app,text="Start/Stop", command=self.play_pause)
        self.state_text = Text(self.app, text="Off")
        logo1 = Picture(self.app, "./img/UZA.png")
        logo2 = Picture(self.app, "./img/inesc.png")
        # ========== Audio ===============
        # Initialization PyAudio Object
        pA = pyaudio.PyAudio()
        # Open microphine and heaset stream
        self.mic = pA.open(format=FORMAT, channels=CHANNELS,
                rate=SAMPLE_RATE, input=True,
                frames_per_buffer=PERIOD_SIZE_IN_FRAME)
        self.speak = pA.open(format=FORMAT, channels=CHANNELS,
                rate=SAMPLE_RATE, output=True)
        # Event loop
        self.app.repeat(10,self.loop_func) #here we made the loop function every 10ms

        # Display the app
        self.app.display()

    #def display(self):
    #    self.app.display()


    #def update(self):
    #    self.app.update()

    # Main loop function
    def loop_func(self):
        # If stop then don't do anything
        if not(self.state):
            return -1
        # Otherwise do the white noise generation
        samples = (np.random.random(size=8300)).astype(np.float32)
        # Send this white noize to the speaker/headset
        self.speak.write(self.volume * self.noise_value *samples,PERIOD_SIZE_IN_FRAME)
        # Listen the input steam of the microphone
        input_data = self.mic.read(PERIOD_SIZE_IN_FRAME,exception_on_overflow=False)
        # Convert into number that can be understand
        data = np.frombuffer(input_data, dtype=np.float32)
        # Compute the energy of the input
        nrj = np.sum(data**2)/len(data)
        # If energy is above the threshold change noize volume
        if nrj > self.db_value:
            self.volume = 0.5
            self.silence_frame = 0
        else:
            self.volume = 0.1
            self.silence_frame += 1
        if self.silence_frame < 10:
            self.volume = 1

    # A simple function to update the start/stop behaviour
    def play_pause(self):
        self.state = not(self.state)
        if self.state == True:
            self.state_text.value = "On"
        else:
            self.state_text.value = "Off"

    # When the slider noise change, update the value
    def slider_noise(self, slider_value):
        if int(slider_value == 0):
            self.db_value =  1
        else:
            self.db_value = 0.1**(int(slider_value))
    # When the slider db change, update the value
    def slider_db(self, slider_value):
        self.noise_value = 0.1 * int(slider_value) #10 ** (int(slider_value) / 20)


win = LombardTool()
