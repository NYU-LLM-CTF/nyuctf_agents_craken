# Docker Web
> A container that contains a web page (http) service. All answers will appear only after you look at the page.

## About the Challenge
We are given a zip code that contain linux directories


[Image extracted text: Task-docker:tar (evaluation copy)
File
Commands
Tools
Favorites
Options
Help
Add
Extract To
Test
View
Delete
Find
Wizard
Info
VirusScan
Task-docker.tar
TAR archive, unpacked size 230,657,470 bytes
Vame
Size
Packed
Type
Modified
CRC32
File folder
noot
File folder
4/18/2022 5.28
dev
File folder
1/30/2023 2.06
etc
523,737
523,737
File folder
1/30/2023 2.06
home
File folder
4/18/2022 5.28
media
File folder
11/30/2022 9.0_
mnt
File folder
11/30/2022 9.0_
opt
File folder
11/30/2022 9.0_
proc
File folder
4/18/2022 5.28
root
3,267
File folder
11/30/2022 9.0_
run
File folder
1/30/2023 2.06
File folder
11/30/2022 9.0_
sys
File folder
4/18/2022 5.28
tmp
File folder
1/29/2023 11.5,
usr
181,323,411
181,323,411
File folder
11/30/2022 9.0_
var
48,807,045
48,807,045   File folder
1/29/2023 11.5,
dockerenv
DOCKERENV File
1/30/2023 2.06
bin
Symlink
11/30/2022 9.0_
Symlink
11/30/2022 9.0_
lib32
Symlink
11/30/2022 9.0_
lib64
Symlink
11/30/2022 9.0,
libx32
Symlink
11/30/2022 9.0,_
sbin
Symlink
11/30/2022 9.0,_]


## How to Solve?
Open the `index.html` file on `/var/www/html` directories and you will notice there is a base64 encoded msg in line `21`


[Image extracted text: animate
CSS
-http:
daneden.me/animate
Version
3.5.2
Licensed under the MIT License
http:
lopensource.org/licenses/MIT
q31iZXJOaG9uIGLzIGEgY29tcGVoaXRpb2AgdzhlcmUgcGFydGljaXBhbnRzIGNvbXBldGUgdG8gc29sdmUgdmFyaW9lcyBjaGFsbGVuZzVzIHJLbGFOZWQgdG8gY3liZXJzZWNIcm OeSwgc3VjacBhc
Copyright (c) 2017 Daniel Eden
lakevframes
bounce{O% . 20% . 53  80%. tofanimation-timing_function:cubic-bezier .215.61.355
1);transform: translateZ(o) 140%.43%{animation-timing-function:cubi]


And if you decode it, you will get the flag

```
vu-cyberthon-23
```