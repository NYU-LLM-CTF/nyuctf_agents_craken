# WxMCTF Forensics 2 - Sneaky Spying
> Shhh, don't tell the MGCI kids, but I spied on one of their conversations! Uhh, I couldn't really understand what they were saying though. Can you let me you what they said? -For educational purposes of course.

> Oh, they also had this open on their phones. I don't know what to make of it though: https://pages.mtu.edu/~suits/notefreqs.html

> Enter any letter characters inside the flag as upper case (e.g: wxmctf{H3LLO})

## About the Challenge
We were given a `wav` file (You can download the file [here](MGCI_Kids_Conversation.wav))and we need to find the music notes

## How to Solve?
To get the flag you can use `Sonic Visualizer` and add a new pane called `Peak Frequency Spectogram`


[Image extracted text: Pane
Layer
Transform
Playback
Help
Add New Pane
Add Waveform
Add Spectrogram
Add Melodic Range Spectrogram
Add Peak Frequency Spectrogram
333333: AlI Channels Mixed
Add Spectrum
<333333: Channel
Switch to Previous Pane
<333333: Channe
Switch to Next Pane
Delete Pane
Ctrl- Shift-D]


Hover your mouse over the yellow light to get an alphabet such as (ABCDEFG) and repeat for each note


[Image extracted text: 293
2960
Time:
0.058
0.150
Bin Frequency: 290.698
296.082 Hz
Bin Pitch: D4-18c
D4+14c
dB: -15 - -14
Phase: 0.658416
2.19302]


```
wxmctf{DECAFE}
```