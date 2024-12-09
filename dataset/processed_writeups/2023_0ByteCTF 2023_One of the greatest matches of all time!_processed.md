# One of the greatest matches of all time!
> The stage was set for an epic showdown as two of the biggest WWE superstars of their generations, The Rock and John Cena, faced off in a match that was billed as "Once in a Lifetime." The atmosphere in the Sun Life Stadium was electrifying, with fans from around the world eagerly anticipating this clash of titans.

## About the Challenge
Given a ZIP file containing 2 images: `onfire.jpg` and `rockvjohn.jpg`. These two files have significantly different file sizes, with `onfire.jpg` being 284 KB and `rockvjohn.jpg` being 2 MB. (You can download the file [here](One of the greatest matches of all time.zip))


[Image extracted text: Filc SizC
284 KB
2MB]


## How to Solve?
The first step is to use the `exiftool` command to display metadata from a file. So, I will use exiftool on both of these files. Here's the command I used:

```bash
exiftool onfire.jpg
exiftool rockvjhon.jpg
```


[Image extracted text: daffainfo@dapos:~/foren-Obyte$ exiftool
onfire. jpg
ExifTool Version
Number
12
40
File Name
onfire. jpg
Directory
File Size
284
KiB
File Modification Date/Time
2023:08:19
15.17.43+07:00
File
Access Date/Time
2023:08:19
15.18:02+07:00
File
Inode Change Date/Time
2023:08
19
15:18:02+07:00
File Permissions
~rw-r~r
File
Type
JPEG
File
Type Extension
jpg
MIME Type
image/ jpeg
JFIF
Version
1.01
Resolution
Unit
None
X Resolution
Resolution
Comment
hattal902
Image Width
1080
Image Height
1931]


The exiftool results for `rockvjohn.jpg` are not interesting, in contrast to the file `onfire.jpg`. There is a comment that says `hatta1902.` There is a possibility that this is a password that can be used on the file `rockvjhon.jpg` considering that the file size is unusual. Here is the command I used, which is `steghide` to perform file extraction because steganographic techniques have been applied to the file.


[Image extracted text: daffainfoddapos:
foren-Obyte$ steghide
~extract
rockvjhon. jpg
Enter
passphrase:
wrote extracted data
to "readme
docx"
~Sf]


My suspicion turned out to be correct, and there is a file with the `.docx` extension generated using the command above. Now, we will move to the file `readme.docx`. When the file is opened, there is a password that locks this file.


[Image extracted text: Password
Enter password to open file
Ilw_(Ubuntulhomel daffainfolforen-Obytelreadme docx
Ok
Cancel]


To unlock this password, we will need to use `John The Ripper` to perform password cracking and `office2john` to convert the document file that will undergo brute force into the john format. Here's the command I used to perform password cracking on the Word document.

```bash
office2john readme.docx > hash.txt
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```

After that, wait for `John` to successfully crack the password. If you want to see the cracked password, then execute the command below.

```bash
john –show hash.txt
```


[Image extracted text: kaliokali)-[~/Desktop]
john
shou hash txt
readme
docx:emiliano
password hash cracked,
0 left]


The password for this document is `emiliano`. Let's open the file using the obtained password.


[Image extracted text: ]


Inside the file, there are seemingly random lines. However, upon closer inspection, these lines are not just lowercase `l` letters; there are also capital `I` letters interspersed within the arrangement of lines. If you use the search feature in Word to look for capital `I` letters, you will find a letter on each page.


[Image extracted text: ]


For example, the image above represents pages 7 and 8, forming the characters `F` and `L`. If all these characters are collected, you will find a shortlink: https://s.id/1FLAGHERE945. If you open this link, you will be redirected to a locked Pastebin page.


[Image extracted text: Locked Paste
Enter password*
Unlock The Paste
paste link to clipboard
Pastebin Home
Copy]


Fortunately, there's a hint: the password for the Pastebin is the same as the password to extract the file.


[Image extracted text: Hint
pw bin
pw extract]


And finally, I entered the password `emiliano`, which is the password I used to unlock the locked document file.


[Image extracted text: Untitled
RIODRWN
AUG 26TH, 2021 (EDITED)
18
NEVER
text
0.04
KB
None
ObyteCTF{ JHON_&_ROck_Ar3_B3st_FrleNld}
Ad]


```
0byteCTF{JH0N_&_R0cK_Ar3_B3st_Fr1eNd}
```