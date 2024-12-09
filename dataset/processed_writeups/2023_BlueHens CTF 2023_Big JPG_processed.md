# Big JPG
> There's more data to this image than what meets the eye.

## About the Challenge
We were given a `jpg` file and we need to find the flag inside the image

## How to Solve?
First, run binwalk or you can use CyberChef and then choose `Extract File` operator. You will see a `xz` file


[Image extracted text: Recipe
Input
lyoyaFXICC_PROFILE
NUL
SOH
NUL
NUL
FHLino
STX
DLE
NUL
NUL
mntrRGB
XYZ
Extract Files
File details
I
STX
ACK
NUL
NUL
acspMSFT
IEC
SRGB
NUL
NUL
NUL
NUL
NUL
NUL
NUL
66
NUL
SOH
NUL
NUL
NUL
NUL
6-HP
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
Images
Video
Audio
Documents
NUL
NUL
NUL
cprt
NUL
SOH
P
NUL
NUL
NUL
3desc
NUL
SOH
lwtpt
NUL
NUL
SOH
NUL
DC4
bkpt
NUL
STX
EOT
DC4
rXYz
STX
CAN
DC4
gXYZ
NUL
NUL
STX
NUL
DC4
bXYZ
NUL
STX
NUL
NUL
NUL
DC4
dmnd
NUL
NUL
STX
NUL
NUL
NUL
pdmdd
NUL
sx A
NUL
NUL
NUL
Applications
Archives
Miscellaneous
vued
NUL
NUL
ETX
NUL
NUL
NUL
view
ETX
NUL
NUL
$lumi
NUL
NUL
ETX
meas
NUL
EOT
F
NUL
NUL
NUL
stech
NUL
NUL
EOT
NUL
NUL
FrTRC
NUL
NUL
EOT
NUL
NUL
FgTRC
Minimum File Size
NUL
NUL
EOT
FbTRC
NUL
EOT
NUL
NUL
Ftext
NUL
NUL
NUL
NUL
Copyright
Name:
big-image jpg
Ignore failed extractions
100
(c)
1998
Hewlett-Packard Company
NUL
desc
NUL
NUL
NUL
NUL
NUL
Size:
1,926,306 bytes
DCZ
SRGB IEC61966-2.1
NUL
NUL
NUL
NUL
DCZ
SRGB
Type:
imagelipeg
IEC61966-2.1
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
Loaded: 100%
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
XYZ
NUL
NUL
NUL
NUL
60
NUL
SOH
NUL
NUL
NUL
SOH
SYN
TYv7
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
NUL
AbC
1926306
6924
TT
Raw
Bytes
Output
extracted_at_Ox50f74.zlib
198 bytes
extracted_at_Ox5f7b6.zlib
26,730 bytes
extracted_at_Ox605ea.Xz
1,531,576 bytes]


Open the `xz` file and you will find 2 images called `key.png` and `flag.jpg`. Input the `key.png` file into AperiSolve or you can `zsteg` tool to extract the key


[Image extracted text: Zsteg
imagedata
text:
222***000>>>
rgb, lsb,Xy
text:
[password:
uR_aLmOsT_tHeRe] '
b4 , b , msb ,Xy
file:
MPEG
ADTS
layer I,
v2 ,
JntStereo
b1 ,]


You got the password! And right now you can use `steghide` or AperiSolve again but don't forget to input `uR_aLmOsT_tHeRe` in the form input


[Image extracted text: Steghide
wrote
extracted
data
to
txt
DOWNLOAD
FILES
"flag .]


Download the result and voilà!

```
UDCTF{lay3r5_0n_lay3r5}
```