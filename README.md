# Lombard effect on speech in Parkinson's disease tool

This tool is used to carry out the study on the effect of Lombard on Parkinson's patients.

### Installation and use

These tools require python (version 3+) to work.

Install the dependencies and launch the tools.

```sh
$ git clone https://github.com/Usanter/Lombard-effect-on-speech-in-Parkinson-s-disease.git
$ git pip install -r requirements.txt
$ python Lombard_effect_tool.py
```

The software can be used with 3 buttons:
- The first slider corresponds to the vocal activity detection (based on the energy of the signal),  higher the value is easier is the threshold
- The second slider corresponds to the power of the white noise, higher correspond to a more powerfull noise signal
- The last button is just a Start/Stop button to control the tool


