# Guatemala
> My friend wanted to install an antivirus for his computer, but the creator of the antivirus was caught!

## About the Challenge
We were given a file without any extension (You can download the file [here](AV))

## How to Solve?
Im using `file` command first to know what is the type of the file


[Image extracted text: (kaliokali)-[~]
cd Desktop
(kaliokali)-[~/Desktop]
file
AV:
GIF image data,
version 89a,
498
498]


As we can see, that file is a GIF file, so I added the `.gif` extension to the file.


[Image extracted text: AV gif
1
02
0  0
100%]


I tried to check the metadata first using `exiftool` command


[Image extracted text: (kaliokali)-[~/Desktop]
exiftool
AV . gif
ExifTool
Version
Number
12.57
File Name
AV . gif
Directory
File Size
1112
File
Modification Date/Time
2023:04:02 04:50:22-04:00
File Access Date/Time
2023:04
02 06:16:54-04
File Inode Change Date/Time
2023
02 06:16:54-04:00
File Permissions
Scio
File Type
GIF
File Type Extension
gif
MIME Type
image/gif
GIF Version
89a
Image
Width
498
Image Height
498
Has
Color Map
Yes
Color Resolution Depth
Bits Per Pixel
Background Color
Animation Iterations
Infinite
Comment
dmlzaHdhQ1RGe3ByMDczYzdfdXJfMI
Frame
Count
Duration
2.04
Image Size
498*498
Megapixels
0. 248
gxRno=]


There is a Base64 msg in the `Comment`. Decode it and you will obtain the flag


[Image extracted text: (kaliokali)-[~/Desktop]
echo
dmlzaHdhQ1RGe3ByMDczYzdfdXJfMIgxRno =
base64
vishwaCTF{pr073c7_
3X1F}]


```
vishwaCTF{pr073c7_ur_3X1F}
```