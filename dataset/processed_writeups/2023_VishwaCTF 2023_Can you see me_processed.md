# Can you see me?
> A magician made the seven wonders disappear. But people claim they can still feel their presence in the air.

## About the Challenge
We were given an image (You can download the file [here](havealook.jpg))

## How to Solve?
In this case im using `binwalk` to know if there is another file inside that image. There result is there is a `zip` file


[Image extracted text: (kaliokali)-[~/Desktop]
binwalk havealook. jpg
DECIMAL
HEXADECIMAL
DESCRIPTION
0*0
JPEG image data,
JFIF standard
1.01
134855
0*20EC7
Zip archive data
at least
V2.0
to extract,
compress
323796
0*4FOD4
End
of Zip archive, footer Length:
(kaliokali)-[~/Desktop]]


And then I tried to open the zip file to see if there is a flag or not in that file


[Image extracted text: 20ECT zip
Archive
Edit
View
Help
Open
Extract
Location:
Name
Size
Type
Date Modified
hereissomethingwav
219.9 kB
WAV audio
08 February 2023]


There is a `wav` file. Extract it and open that file using Sonic Visualizer -> Spectogram to read the flag


[Image extracted text: File
Edit
View
Pane
Layer
Transform
Playback
Help
~II
F
Fi
0 s %
3
6
4 + 0
A
W
I
W
4,985
22050Hz
1,442
31808
0335
1.442131808
9905
9474
9065
8634
8204
113
1342
6912
6481
6050
5620
5189
389
2005
vishwac|iFindw_ydu 533_m3}
335_
904 
473 _]


```
vishwaCTF{n0w_y0u_533_m3}
```