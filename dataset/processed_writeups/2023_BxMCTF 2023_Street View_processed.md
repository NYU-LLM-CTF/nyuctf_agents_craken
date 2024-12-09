# Street View
> One day, clides was doing some detective work to try to catch the person who stole the 2 rubber duckies from the BxMCTF prize pool. He was doing some OSINT and he stumbled upon this street view image from ClaudsVille on Dread. Apparently, this image was sent from the thief.

> Can you help clides to find out where the image was taken?
 
> Submit the domain name of the company that owns the building as the flag, wrapped in ctf{}

## About the Challenge
We were given an image file and we need to submit the domain name of the company

## How to Solve?
As usual, check the metadata of the image first


[Image extracted text: XMP Toolkitr
Image:ExifTool 12.60
Latitudeg
430 52' 38.32" N
Longitudez
790 24' 31.00" W
Image Sizez
1203x709]


As you can see there are 2 unique metadata called `Latitude` and `Longitude`. Now go to Google Maps and go to that location, check the owner of the building and get the domain name


[Image extracted text: 51*06'37.1"N 17*03'18.9"E
X
Overview
Reviews
About
Directions
Save
Nearby
Send to
Share
phone
Dine-in
Kerbside pickup
No-contact delivery
Habibi Doner
plac Grunwaldzki 4a, 50-384 Wroclaw; Poland
Open
Closes 11PM
Place an order
Menu
habibidonercom
habibidonercom
+48 666 699 786
4364+44 Wroclaw; Poland
most Grunwaldzki
Send to your phone
Add a label
372
Suggest an edit
Layers
Go]


```
ctf{walmart.ca}
```