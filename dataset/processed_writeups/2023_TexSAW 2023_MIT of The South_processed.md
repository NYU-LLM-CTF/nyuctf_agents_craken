# MIT of The South
> Welcome to UTD! We like to call ourselves the MIT of the South (not really). The flag for this challenge is hidden in one of the classrooms, can you find it?

## About the Challenge
We were given a very simple website that contains only 1 image


[Image extracted text: 6 +
C
Not secure
18.216.238.24 1004/webpage/files/dir/indexhtml
1 * & * = 0]


## How to Solve?
First I checked some interesting files for example `sitemap.xml` or `robots.txt`. And I found there is a `robots.txt` file


[Image extracted text: 2 >
C
Not secure
18.216.238.24.1004/webpage/files/dir/robotstxt
Robots
There
are
robots
here
Only
Temoc
and
his
army
tobors!]


After getting a little stuck, I decided to check `tobors.txt` and luckily, I obtained a list of endpoints.


[Image extracted text: k 
C
Not secure
18.216.238.24 1004/webpageffiles/dir/tobors txt
lad/
lad/1.100/
lad/1.101/
lad/1
102/
ad/1.103 /
lad/1.104/
lad/1.105 /
lad/1.106/
/ad/1
107 /
[ad/1.108_
lad/1.109 /
lad/1
110/
lad/1.111/
lad/1.112/
lad/1.113/
lad/1.114/
lad/1.115 /
lad/1.116/
lad/1.117 /
lad/1.118/
lad/1.119/
[ad/1.120/
lad/1.121/]


I manually checked the endpoints one by one but the response is always `There's nothing written on the board`. So I used `ffuf` here

```shell
ffuf -w endpoints.txt:FUZZ -u http://18.216.238.24:1004/webpage/files/dirFUZZ -fl 29
```


[Image extracted text: Ci19t
V2.0. 0-dev
Method
GET
URL
http://18.216.238.24:1004/webpage/files/dirFUZZ
Mordlist
FUZZ:
/home/kali/Desktop/cok.txt
Follow redirects
false
Calibration
false
Timeout
Threads
Matcher
Response
status:
200,204,301,302
307
401,403
405
500
Filter
Response
lines:
[Status:
200 _
Size:
420 ,
Mords:
13 ,
Lines: 26, Duration:
286m5
FUZZ:
lad/
[Status:
200 _
Size:
427 ,
Mords:
16, Lines: 26, Duration: 277m5
FUZZ:
latc/
[Status:
200 _
Size:
419 , Words:
15, Lines: 26, Duration:
313m5
FUZZ:
/be /
[Status:
200 _
Size:
428 , Words:
16 , Lines: 26, Duration: 258m5
FUZZ:
Icbl/
[Status: 200, Size:
428 , Words:
16, Lines: 26, Duration:
323m5
FUZZ:
Icbz/
[Status: 200, Size:
428 , Words:
16, Lines: 26, Duration: 293m5
FUZZ:
Icb3/
[Status:
200 _
Size:
447 , Words:
18, Lines: 26,
Duration:
274m5
FUZZ:
ecsn/
[Status:
200 _
Size:
447 , Words:
18, Lines: 26, Duration:
329m5
FUZZ:
ecss/
[Status:
200 _
Size:
475
Words:
18, Lines:
30 , Duration: 273m5
FUZZ:
ec55/4.910/
[Status:
200 _
Size:
446 ,
Mords:
18, Lines: 26 ,
Duration: 263m5]
FUZZ:
ecsm/]


The flag was located in `/ecss/4.910`


[Image extracted text: page/files/dir/ecss/4.910/
Someone wrote something on the board. It says texsaw{wooOoOoOoOoOOoOooooOoooOooosh}]


```
texsaw{woo0OOo0oOo00o0OOOo0ooo0o00Osh}
```