# funding secured
> Someone in our company leaked some very sensitive information. We absolutely cannot let this stand.

> Thankfully our monitoring software intercepted the screenshot that was leaked. An old engineer of ours did write some kind of watermarking for screenshots but we have no idea how it works. Can you figure it out?

## About the Challenge
We were given an image (You can download the image [here](captured.png)) and when I scanned the image using Aperisolve, I found something interesting in the `zsteg` output


[Image extracted text: Zsteg
imagedata
text:
xxXrrr
b1,r, msb,Xy
text:
(*LLUejo"
b1, rgb , Isb,xy
text:
creator.txtUtir"
b2
r,msb, XY
text:
UUUUUU}UUu
b2 , 9, msb, XY
text:
} WWu_ ]WJw"
b2 , b , msb,xy
text:
UUUUUUWU
b2 , rgb, msb,xy
text:
JUUUWUUUWUU"
b2 , bgr , msb,xy
text
U] JUUUWUUuUUu'
b4 , r , msb,XY
text:
repeated
10 times
b4 , 9,
msb,xy
text:
repeated
10
times
b4 , b , msb
Xy
text:
repeated
12 times
b4
rgb, msb,xy
text:
'w
repeated
33
times
b4 , bgr , msb,xy
text:
{
'w
repeated
34 times]


## How to Solve?
So, I believe there's a file inside this image. Initially, I tried using `binwalk` to extract the file, but failed. It seems like we need to use LSB steganography to extract the file.

So I used this [website](https://stegonline.georgeom.net/extract) and then, using the `Extract Data` feature voilà! I found a ZIP file.


[Image extracted text: settings appropriately. The final extracted data is checked against some basic file
headers, and so the filetype can be automatically determined:
Please note that Alpha options are only available if the image contains transparency:
5
4
3
2
Pixel Order
Bit Order
Bit Plane Order
Trim Trailing Bits
Row
MSB
No
Go
Results
No file types identified
The results below only show the first 2500 bytes. Select "Download" to obtain the
full data.
Ascii (readable only):
PK.
g .
creator
txtUt.
na
b.
bn.
bux.
-RP
PJ . JM, IM
0 .
.KM
U.RPrI.
L.Q.M,*.
S.AS.
.V.
Eb.P.
PK.
IGG .
PK.
Hex (Accurate):
0d09005046030414000800080dedbcb3540000000000000000670000000600200063
726561746f722e74787455540d00076e0d8762870d87626e0d8762757806000104f5
0100000414000000abe65250504a2e4a4d2c494d894faa8ccf4bcc4d556252507249
Download Extracted Data]


But when I extracted it, I only got 2 files: `exif.txt` and `creator.txt`, But in the ASCII text, there's another file called `flag.txt`. So I decided to use CyberChef and then use `Extract LSB` option


[Image extracted text: Recipe
Input
PNGS
Extract LSB
File details
SUB
NUL
NUL
NUL
RIHDR
NUL
NUL
STX
NUL
NUL
NUL
STX
NUL
NUL
NUL
42+,
NUL
NUL
FziCCPICC
Profile
NUL
NUL
X
Jhls & Huge!rec lux lcamcd that IHE ELCH MUSEeoine t0 jrCurethc compari. Hctodus
Colour Pattern #1
Colour Pattern #2
Colour Pattern #3
ncndineJeltlurad Ware abou: to &o haher than
GML byend %u ? eek Get your tees Ir
YWw| SE
SYN
[RIh
H
2
"ZH
iE
DLE
xD
I
bBPt
E
ENQ
X,
"XNU
Ue
R
B
EZttbi
Toca
ut
CaMH@x}iyofi7w4 | sa*3c-
U
SOH
,ac)P]
NUL
0x
ENQ
Name:
captured png
Epog' t
SYN
e)A-
NUL
:0an
NAK
2v | | #.2Dy]PY
EOT
@2at2oify) u
STX
NUL
2
a
Colour Pattern #4
Pixel Order
Bit
Size:
26,704 bytes
NAK
NUL
06 |
NUL
NUL
EOT
ods
Row
d*l
b erx 9F
DLE
amx 
Eox @HMy: I
SOH
Ox<y6
NUL
0]
g
NAK
0 3 ;
SUB
AnR=
Type:
imagelpng
X
Loaded:
100%
iH
0
NUL
a
DLE
EEEWa-
DLE
;@}
Ao
fiiui
iae
boeu
Extract Files
GVEski
ETX
k&
ACK
ETX
DCZ
A
ETX
oy/y
DCZ
a.0; Dh"yT-*
05 . SOEU
CAN
e
fEFor
n
t@y
NUL
Images
Video
Audio
Documents
@@"eT2z
53+80-
+
ETB
SYN
St)A
RIU
if
DCZ
Gp ! -f-N
NAK
ETB
6.X'P
"NU, iODoBk?a
I-2i +0Uuz" IMfkiz
SYN
SUB
'V
NAK
bxA6 a Xe
p!vUa FktF
SYN
8t Erx
re
x~
DC3
OEPu}-OK
N/NT ( =
BEL
0 ,
DC2
sc5e@
Applications
Archives
Miscellaneous
()Je
14
71 VVE(e'
DCI
XEEF-E
FVW 
2
DLE
J
DCJ
Sv>E
DC?
OsqaL
DC2
~NC
NAK
ENQ
+84003
ETB
0) . AelegE
abc
26704
=
103
TT
Raw Bytes
LF
Minimum File Size
Ignore failed extractions
100
Output
9
filels)
found
extracted_at_Ox3.zip
2,317 bytes
Ldj
extracted_at_Ox3. jar
2,317 bytes
extracted_at_0x93.Zip
2,173 bytes
extracted_at_Oxa3.zip
2,157 bytes
extracted_at_Oxa3. jar
2,157 bytes
STEP
BAKEI]


Download the zip file and then read `flag.txt` file

```
flag{what_came_first_the_stego_or_the_watermark}
```