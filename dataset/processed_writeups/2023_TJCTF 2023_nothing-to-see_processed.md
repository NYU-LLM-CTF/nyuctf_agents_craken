# nothing-to-see
> nothing to see here, just move along

## About the Challenge

We have given a image like this and we need find the flag from the given image


[Image extracted text: nothing to see here]


## How to Solve

Fist you need do `exiftool` on this image, and you'll find interesting information


[Image extracted text: sinon@LAPTOP- 2VOH1439: /mnt/d/afbountylctf/TJCTF$
exiftool nothing-png
ExifTool
Version
Number
11.88
File
Nane
nothing-png
Directory
File
Size
15 kB
File Modification Date/Time
2023:05:26 07:05:28+07:00
File
Access Date
Time
2023:05:28 11:23.41+07:00
File Inode Change Date/Time
2023:05:26 07:05.42+07:00
File
Permissions
rWxrWxrWX
File Type
PNG
File Type
Extension
png
MIME Type
image/png
Image Width
560
Image Height
450
Bit Depth
Color Type
RGB with Alpha
Compression
Deflate
Inflate
Filter
Adaptive
Interlace
Noninterlaced
Title
panda_dozb3ab3
Warning
[minor]
Trailer data after PNG IEND chunk
Image Size
560x450
Megapixels
0.252]


You'll see the Title is `panda_d02b3ab3`, it will be use after this

After that you can perform `foremost` to see if there any extracted file


[Image extracted text: sinon@LAPTOP - 2VOH1439
[mntfd/afbountyfctf/TJCTF$
foremost nothing-png
Processing: nothing-png
foundat-flag-txtUt]


You'll find the zip file which is locked, the password is use from what we've got from exiftool


[Image extracted text: Enter password
panda_d02b3ab3
Showv password]


And we got flag


[Image extracted text: xflag txt
Notepad
File
Edit
Format
View
Help
flag{the_end_is_not_the_end_4c261b91}]


```
tjctf{the_end_is_not_the_end_4c261b91}
```