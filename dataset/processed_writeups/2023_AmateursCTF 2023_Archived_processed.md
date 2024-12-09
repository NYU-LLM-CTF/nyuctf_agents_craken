# Archived
> This challenge has been archived.

## About the Challenge
We need to find archived challenge using OSINT technique

## How to Solve?
At first im using web.archive.org to find archived website but I found nothing here


[Image extracted text: INTERN ET
A R C H [V E
Explore more than 818 billion web pages saved over time
DONATE
Ibyuachhhuhl
https {ictf amateurs teami
Calendar
Collections
Changes
Summary
Site Map
URLs
Saved 2 times June 30, 2023
Joo
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
JAN
FEB
MAR
APR
17
27   28
21
17
27
MAY
JUN
AUG
22
23   24
25   26   27
20   21
22   23   24
17
21   22
21   22   23
24   25
26   27   28
27   28
27   28
29]


And then I tried to googling about `AmateursCTF` and I found this search result


[Image extracted text: "AmateursCTF"
Gost; amateursC TF{yOu-fOunD_m3;bu7:d1D U r34Lly?}
Gost
You visited this page on 7/19/23.
https IlmdShashing net >
Blame website's content
tiger128,4 hash decoder and calculator
4 days ago
Decode Tiger128,4. Reverse lookup, unhash; decode; or "decrypt"
Tiger128,4,
26fd9a4fc6fb609dcce73fedfo690f8618eeb840 ; Tiger128,4, amateursCTF{
Internet Archive
https Ilarchive org
details
opensource
Community Texts
Free Books
An archive of a canned solution
challenge from AmateursCTF 2023. For more info check the
CTFtime. https Ilctftime orglteam/166729/
You visited this page on 7/19/23.]


Result from archive.org? interesting. And then we got this archived [challenge](https://archive.org/details/amateurs-ctf-2023-archive-july-13-2023.7z)


[Image extracted text: AmateursCTF 2023 Archived Challenge July 13 2023
Favorite
Share
Flag
by smashmaster
Publication date
2023-07-13
Usage
Public Domain Mark 1.0
0
Views
Topics
ctf, capture the
security
Collection
opensource
Language
English
DOWNLOAD OPTIONS
An archive of a canned solution challenge from AmateursCTF 2023. For more info check the CTFtime.
7Z
file
https:Ilctftime orglteam/166729/
TORRENT
file
Addeddate
2023-07-14 05.36.23
Identifier
amateurs-ctf-2023-archive-july-13-2023.7z
SHOW ALL
5 Files
Identifier-ark
ark:/13960/s2396910qb1
Scanner
Internet Archive HTMLS Uploader 1.7.0
Original
Year
2023
flag;]


Download the archived challenge, and then read `flag.txt` to obtain the flag


[Image extracted text: AmateursCTF2023-Archive-July-13-2023.7zlarchived
solid 7-Zip archive; unpacked size 204 bytes
Name
txt
solve txt
File
Edit
View
challenge:yml
flag.txt
amateursCTF{archlv3d_rlght_b3for3_th3_start}
flag:]


```
amateursCTF{arch1v3d_r1ght_b3f0r3_th3_start}
```