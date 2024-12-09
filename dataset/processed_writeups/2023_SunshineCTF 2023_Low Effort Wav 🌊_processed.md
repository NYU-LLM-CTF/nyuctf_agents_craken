# Low Effort Wav 🌊
> Last year we went all-out and created a JXL file that had too much data.

> That was too much effort. Shuga had to go and create a custom file that was altered, that's too much work, and is too passé. Also an astounding 286 guesses were made against 9 correct answers. That was too many.

> This year, we used an already existing vulnerability (edit: aaaaaaaaaand it's patched, and like a day after we made this challenge... which was months ago), for minimum effort. And the flag, dude, is like, fully there, when you find it. Not half there. No risk of guessing.

> This year, we introduce:

> The low-effort wave 🌊
> Ride the wave man. 🏄‍♂️🏄‍♀️🌊

> The wave is life. The waves are like, sound, and like water, and like cool and refreshing dude.

> But waves are hard to ride
> So listen to them instead, crashing on the seashore. Listen to the music of the sea. Like the theme this year is music or something. So I theme this challenge, like, minimum effort music. Listen to this attached .wav file. It's amazing. Or so I've heard. Or rather, haven't. Something's broken with it. I don't know dude.

> It also doesn't work. Can you fix this for me? I think there's a flag if you can find it.

> Hints
> There will be no hints given for this challenge by judges. The flag is in standard sun{} format. If anything, we've already given you too much data.

## About the Challenge
We got a file called `low_effort.wav` (You can download the file [here](low_effort.wav)) and if we run `file` command:


[Image extracted text: daffainfo@dapos:
mntlclUsers_
Muhammad
Daffa/DownLoads$
file Low_effort
wav
Low_effort
wav:
PNG image data_
465
X 803 ,
8-bit/color RGBA ,
non-interlaced]


And if we run `exiftool` command:


[Image extracted text: ExifTool
Version
Number
12.40
File
Name
Low_effort
wav
Directory
File Size
244 KiB
File Modification Date/Time
2023:10:07 22:02:43+07
00
File
Access
Date/Time
2023:10:09 19:16:52+07
00
File
Inode
Change Date/Time
2023:10:07 22:02:49+07
00
File
Permissions
~rwxruXTWX
File Type
PNG
File Type Extension
png
MIME Type
image/png
Image Width
465
Image Height
803
Bit Depth
Color Type
RGB with Alpha
Compression
Deflate/Inflate
Filter
Adaptive
Interlace
Noninterlaced
SRGB Rendering
Perceptual
Significant Bits
8 8 8 8
XMP Toolkit
Image: :ExifTool 12.59
Original File
Name
Screenshot_20230319-223111.png
Exif Byte
Order
Big-endian (Hotorola,
MM)
X Resolution
72
Resolution
72
Resolution Unit
inches
Cb Cr
Positioning
Centered
Unique
Camera Model
Google Pixel
Warning
[minor]
Trailer
data after PNG IEND
chunk
Size
465x803
Megapixels
0.373
Image]


There are an interesting information like `Warning : [minor] Trailer data after PNG IEND chunk` and `Unique Camera Model : Google Pixel 7`

## How to Solve?
To get the flag, I took advantage of [CVE 2023-21036](https://en.wikipedia.org/wiki/ACropalypse), which is a vulnerability in Markup (Screenshoot editing tool in Google Pixel). And im using this [tool](https://github.com/frankthetank-music/Acropalypse-Multi-Tool) to recover cropped image


[Image extracted text: Acropalypse Multi Tool
SnTu6a
Touay al TOZTT
Save Image
Half screen?
Select Image
solarbonite
at
low_effort png
Ican take it horizontal
Google Pixel
With keyboard
Here'$ the flag that no one will guess
inda of
Original Width:
thing
Shuga
at 10.28 P
Keep it secret though
Make sure to redact it
1080
sunfwell_that_was_low_effort}
Ye
Original Height:
Message #challenge-creation
GIF
solarbonite
at
2400
Here's the
that no
W
ER vyu vo
A
S
D
F G H J Ki
Acropalypse Now!
Keep it secret though
2 X C V B N M
2123
English
Make sure to redact it
Reconstructed the image successfully
Today
Today
Today
flag -
thing]


```
sun{well_that_was_low_effort}
```