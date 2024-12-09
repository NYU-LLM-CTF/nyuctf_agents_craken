# Selfie
> One day, clides secretly plugged a rubber ducky into Claudio Pacheco's laptop and gained control. While browsing through his files, he found this selfie which contains some secret information.

> Can you help him find the secret information hidden in the selfie?

## About the Challenge
We were given a `zip` file that contains an image and we need to find the flag inside the image

## How to Solve?
To solve this problem, we can use `exiftool` to check the metadata of the file. And as you can see there is weird metadata called `License`


[Image extracted text: MIME iypem
Imageijpeg
Exif Byte Orderz
Big-endian (Motorola,; MM)
XMP Toolkits
Image:ExifTool 12.60
Licenser
Y3Rme2SxaUoyQnQyaVZEa2d6fQ
Image Widths
1241
Image Heightz
1157
Encoding Processz
Progressive DCT; Huffman coding]


Decode the msg using `Base64` to read the flag


[Image extracted text: Decode from Base64 format
Simply enter your data then
the decode button_
Y3Rme25xaUoyQnQyaVZEa2d6fQ
For encoded binaries (like images, documents, etc:) use the file upload form
UTF-8
source character set 
Decode each line separately (useful for when you have multiple entries).
Livve mode ON
Decodes in real-time as you type or paste (supports only
DECODE
Decodes your data into the area below:
ctf{ngiJZBtZiVDkgz}l
push]


```
ctf{nqiJ2Bt2iVDkgz}
```