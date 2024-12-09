# Hidden Figures
> Look at this fan page I made for the Hidden Figures movie and website! Not everything is what it seems!

## About the Challenge
We've got a website about a movie called `Hidden Figures`


[Image extracted text: HIDDEN
FIGURES
THE HISTORY
THE Book
THE AUthOR
THE MOVIE
PRESS
CONTACT
F I G
U R E
S
#1 NY Times Bestseller!]


## How to Solve?
At first I got stuck for a very long time because this website was a static website and there is some weird JavaScript file and I still got nothing lol. And then I check every image on the website

```
data:image/png;base64,/9j/4AAQSkZJRgABAQEAlgCWAAD//gBWRmlsZSBzb3VyY2U6IGh0dHA6Ly9jcmdpcy5uZGMubmFzYS5nb3YvY3JnaXMtZWRpdC9pbmRleC5waHAvRmlsZTpHUE4tMjAwMC0wMDE5MzIuanBn/9sAQwAGBAUGBQQGBgUGBwcGCAoQCgoJCQoUDg8MEBcUGBgXFBYWGh0lHxobIxwWFiAsICMmJykqKRkfLTAtKDAlKCko/8AACwgA8AEsAQERAP/EAB0AAAEFAQEBAQAAAAAAAAAAAAUCAwQGBwgBAAn/...
```

And then I tried using `binwalk` on every image, and I found the flag by using the image on line 609.


[Image extracted text: /9j/4AAQSkZJRgABAQEAlgCWAAD/ /gBWRmlsZSBzb3VyY2U6IGhOdHA6Ly9jcmdpcySuzGMubmFzYSSnb3YvY3JnaXMtZWRpd
From Base64
copbmRlecSwaHAvRmlsZTpHUEAtMjAWMCOWMDESMZIuanBn/9SAQWAGBAUGBQQGBgUGBWcGCAoQCgoJCQoUDg8MEBcUGBgXFB
Alphabet
YWGholHxobIxWFiAsICMmJykqKRkfLTAtKDAlkcko/8AACWgASAESAQERAP/EABOAAAEFAQEBAQAAAAAAAAAAAAUCAWQGBwg
A-Za-20-9+/=
BAAn /XABJEAABAWMCAWYCCAMGAWYHAQABAgMEAAURBiESMUEHEy JRYXEUgSMyQlKRobHBFWLRCCQZCOLhFkNTFZRZgZLSJSZE
VKLC8PH/2gAIAQEAADSAOp/Vdgbvj4F8/WDlpHZ1GOsrLxYbtThVSEJFJ/42g8kWNWRSqH9KQ9rFtIPd2FJx65,
aoFxlnORDe
cgbejuohBKEKzufKhzngyannMOKm6ciRlhWEjuzuPxoOLxqRwDurZDTZs
'06iVqpwbRoyPzkforxter3DAFsI3/wckn+lPIt
Remove
non-alphabet chars
Strict mode
2qHMcUoD2SB+1OJO9qJ3HHCHBSApWaRu6z9JcXux3jSXoWUAR3k14/6qeT2dJV/is3s+9Fo9gbszEBhtYU3sUlxjGTk4zv8qs
NgtLFytzkvgALayccehzVLufZrpuUgKuMZCWZDjiURjz6OxZNGGUhW19pbUBEZSSKwlskAKkZxzPMZNVa/WD8KFznxro1HTFj
thsqbx41FScnPkMA/GrGEDGOZT+FJUwjKSUDnSV8plvitoPwplbSVqWEAk8gBTTZTL JWAOJf /TTz+ZovckFCkAd7tKOiE7DS+
Extract Files
dQXHif+YypgQqopzoeR4h_
KkngKB364liNSDTuenosh+lNZawg
CAOGISg9SkAfnUS6BNJWmCARSISAPIqM7bJpSxkJHqAP2q
IgaZpSojp/1k/tURURZAUIKmsloceATkAA/r+FQmret DjfeJSOOKJUE88bedIXZxk8UhzgkgVFdtTQ+S46fmB+lRLQI6c+FZ
91mmTDj5 /wh+JrptembWkSdUzPgyxXgtWnmTASEMEebqfeosn/hlr/Wcqhf-QNequelzuzyYsgkk/tUdzvol46VK73ISMnhZP
Images
Video
Audio
Documents
9KDWntvoncnXmaSJayljOWMZ
EOTPaFakqAW4EtxkeFI/ekKZRGskNWSr1KgP2q092g29/hgPqVSZWf6UwvXGp3Wy tgySro
51824
Raw Bytes
Applications
Archives
Miscellaneous
Output
I]
CAG
7C GEL
DAE
"JpS
13,+00
Dy Les
LT
Minimum File Size
Ignore failed extractions
100
extracted_at_Ox3c7e.png
23,380
bytes
flag{e62630124508ddb3952843f183843343}
extracted_at_Ox3ca7.zlib
102
bytes
STEP
BAKEI
Auto Bake
41m5
T
Raw Bytes]


```
flag{e62630124508ddb3952843f183843343}
```