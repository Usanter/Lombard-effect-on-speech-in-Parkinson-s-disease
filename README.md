# Lombard effect on speech in Parkinson's disease tool

This tool is used to carry out the study on the effect of Lombard on Parkinson's patients.

### Installation and use

These tools require python (version 3+) to work.

Install the dependencies and launch the tools.
For mac OS user:

1 - Install XCode in the app store
2 - Run the following command 
```sh
$ git clone https://github.com/Usanter/Lombard-effect-on-speech-in-Parkinson-s-disease.git
```
or dowload the zip and extract it

3 - Go where you download it and open a terminal here
```sh
$ pip3 install -r requirements.txt
$ python3 Lombard_effect_tool.py
```

For windows user:
```sh
Click on the Lombard_tool.exe
```

The software can be used with 3 buttons:
- The first slider corresponds to the vocal activity detection (based on the energy of the signal),  higher the value is easier is the threshold
- The second slider corresponds to the power of the white noise, higher correspond to a more powerfull noise signal
- The last button is just a Start/Stop button to control the tool


