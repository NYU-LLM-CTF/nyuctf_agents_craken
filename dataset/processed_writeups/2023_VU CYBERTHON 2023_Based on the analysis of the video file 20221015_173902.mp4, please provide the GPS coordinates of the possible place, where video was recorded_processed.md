# Based on the analysis of the video file 20221015_173902.mp4, please provide the GPS coordinates of the possible place, where video was recorded
> The main task is to perform the forensic information technology examination on the acquired image of mobile phone. Two suspects (two men) were arrested near Lithuanian and Republic of Belarus border. The truck with stored weapons was taken. During the seizure, a mobile phone without identification tags was founded on the ground near the truck. A criminal case has been opened related to the international illegal arms trade. Please help to find the relevant information for the case, examine the digital dump acquired from the seized phone memory and answer the questions below.

> GPS coordinates. From investigators of the current case, it was determined that the cargo truck recorded in the video file userdata\media\0\Download\20221015_173902.mp4 is the same one that was detained at the time of the crime. Analyze this file and answer the question below.

> Based on the analysis of the video file 20221015_173902.mp4, please provide the GPS coordinates of the possible place, where video was recorded? (please provide the GPS Latitude and Longitude in decimal degrees format (dd.dddd, dd.dddd).

## About the Challenge
We need to find the location of the video

## How to Solve?
First i export the file from FTK Imager (You can find the file on `/userdata/root/media/0/Download` folder)


[Image extracted text: File List
Name
Size
20221015_173902 mna
87,102
Telegramapk
Export Eiles:
67,572
Telegram (1).all
Export File Hash List _
67,572
curriculum vitai
Add to Custom Content Image (ADD)
18,873
Magisk-V25.2.apk
11,014
Magisk-25.2(25200).apk
11,014
tanksmp4
10,314
KingoRootapk
6,460
KingoRoot-Z.apk
6,460
KingoRoot-I.apk
6,460]


After that, check the metadata using `exiftool`. There is GPS location in the metadata


[Image extracted text: Audio Sample
Rate
48000
Image Size
1920*1080
Megapixels
2.1
Bitrate
14.3 Mbps
GPS Latitude
54 deg
34. 68"
GPS Longitude
25 deg 24
29.88"
Rotation
GPS Position
54 deg
49
34.68"
25 deg 24
29. 88"
Avg]


```
54.8263, 25.4083
```