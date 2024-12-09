# replace-me
> I knew I shouldn't have gotten a cheap phone :/

## About the Challenge
We were given a boot image file (You can download the file [here](dist)), and we need to find the flag there

## How to Solve?
First, you can use `file` command in linux to find out the type of file to be analyzed


[Image extracted text: dist
Android bootimg
kernel
ramdisk,
page
size
2048
cmdline (console-ttyHSLO, 115200, n8 androidboot
hardware-mako Lp
j-67677
user_
debug-31)]


When I solved this challenge yesterday, I used `binwalk`, but if you are using the intended way, you can use `mkbootimg`. Now, to extract the files using `binwalk`, here is the command I used to extract the files from dist:

```bash
binwalk -e dist
```


[Image extracted text: daffainfo@dapos:
/dist$
binwalk
~e
dist
DECIMAL
HEXADECIMAL
DESCRIPTION
Oxo
Android bootimg ,
kernel
size
6009416
bytes
kernel
addr
0x80208000
ramdisk
size
491824
bytes
ramdisk
addr
0x81800000
product
name
2048
0x800
Linux
kernel
ARM boot
executable ZImage (little-endian)
18399
Ox47DF
gzip compressed
data
maximum compression ,
from
Unix
last modified:
1970-01-01
00 : 00 : 00
null
date)
6012928
OxSBCOOO
gzip compressed data,
from Unix,
last modified:
1970-01-01
00: 00:00 (null
date)]


And then extract the extracted file again called `5BC000` using binwalk

```bash
binwalk -e 5BC000
```


[Image extracted text: ~daffainfo@dapos
Idist/_dist
extracted$ binwalk
SBCOOO
DECIMAL
HEXADECIMAL
DESCRIPTION
Oxo
ASCII cpio
archive (SVRU with
no CRC)
file
name
charger"
file
name
Length:
"Ox00000008"
file size:
"Oxoooooood"
136
0x88
ASCII
cpio archive (SVRU with
no
CRC)
file
name
"data"
file
name
Length:
"0xoooo0005"
file
size:
Oxoooooooo"
252
OxFC
ASCII
cpio
archive (SVRU with
CRC)
file
name
"default
prop"
file
name
length:
"Oxoooooood"
file
size:
"Ox00000155"
720
OXZDO
ASCII
cpio archive
(SVR4
with
no
CRC)
file
name
"dev"
file
name
Length:
"0xo0000004"
file size:
"Oxoooooooo"
836
0x344
ASCII
cpio
archive
(SVR4 with
no
CRC)
file
name
"file
contexts"
file
name
Length:
"Oxoooooode"
file size:
"Oxoooo4odf"
17568
0x44AO
ASCII
cpio archive (SVRU with
no
CRC)
file
name
"fstab.mako"
file
name
Length:
"Oxooooooob"
file
size:
"Oxoooooa41"
20320
Ox4F6o
ASCII
cpio
archive
(SVR4 with
no
CRC)
file
name
"init"
file
name
length:
"Oxoooooo05"
file
size:
"0x00031948"
223516
0x3691C
ASCII
cpio archive (SVR4
with
CRC)
file name:
"init
environ
rc"
file name length:
"0x00000010"
file size:
"0x000003d5"
224628
0x36074
ASCII cpio
archive (SVRU with
no
CRC)
file
name
"init.mako.rc"
file
name
length:
"Oxoooooood"
file
size:
"Oxooo03bc8"
240056
0x3A9B8
ASCII
cpio archive
(SVR4 with
no
CRC)
file
name :
"init.mako
usb
rc"
file
name
Length:
"0x00000011"
file
size:
"0x00001745"
246144
0x3C180
ASCII
cpio
archive (SVRU with
CRC)
file
name
"init.rc"
file
name
Length:
"Ox00000008"
file size:
"Oxooo05sde"
268248
0x41708
ASCII
cpio archive
(SVR4
with
no
CRC)
file
name
"init trace.rc"
file
name
Length
"Oxoooooobe"
file size:
"0x00000787"
270300
Ox41FDC
ASCII
cpio
archive (SVRU with
no
CRC)
file
name
"init.usb.rc"
file
name
Length:
"Oxoooooooc"
file size:
Oxooooof2d"
274312
0x42F88
ASCII
cpio archive (SVRU with
no
CRC)
file
name
"init
zygote32
rc"
file
name Length:
Ox00000011"
file
size:
"0x0000012d"
274744
0x43138
ASCII
cpio
archive (SVRU with
no
CRC)
file
name
"proc"
file
name
Length:
"Oxoooooo05"
file
size:
"Oxoooooooo"
274860
0x431AC
ASCII
cpio archive (SVR4
with
CRC)
file name:
"property
contexts"
file
name
Length:
0x00000012"
file size:
"Ox00000a99"
277704
0x43ccC8
ASCII cpio
archive (SVRU with
no
CRC)
file
name
"res"
file
name
Length:
"Oxoooooo0l"
file size:
Oxoooooooo"
277820
0x4303C
ASCII
cpio archive
(SVR4 with
no
CRC)
file
name
"res/images"
file
name
Length:
"Oxooooooob"
file
size:
"Oxoooooooo"
277944
0x43DB8
ASCII
cpio
archive
(SVR4 with
no
CRC)
file
name
"res/ images/charger"
file
name
length:
"Ox00000013"
file
size:
"Oxoooooooo"
278076
0x43E3C
ASCII
cpio archive (SVRU with
CRC)
file
name
"res/images/charger/battery_fail.png"
file name Length:
"0x00000024"
file
size
0x0000185c"]


And the flag was located in `/cpio-root/res/images/charger` directory


[Image extracted text: Namne
Dale mnoumed
ype
JizE
battery_faillpng
10/9/2023 5.26 PM
PNG File
KB
battery_scale png
10/9/2023 5.26 PM
PNG File
1 KB
battery_failpng
100%
bctf{gr33n_rObOt_phON3}
2]


```
bctf{gr33n_r0b0t_ph0N3}
```