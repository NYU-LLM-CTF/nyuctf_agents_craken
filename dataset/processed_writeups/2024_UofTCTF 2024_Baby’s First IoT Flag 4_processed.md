# Baby’s First IoT Flag 4
> Part 3 - Submit the command used in U-Boot to look at the system variables to port 1337 as a GET request ex. http://35.225.17.48:1337/{command}. This output is needed for another challenge. There is NO flag for this part.

> Part 4 – Submit the full command you would use in U-Boot to set the proper environment variable to a /bin/sh process upon boot to get the flag on the webserver at port 7777. Do not include the ‘bootcmd’ command. It will be in the format of “something something=${something} something=something” Submit the answer on port 9123.

## About the Challenge

As you can see the part 3 and part 4 is merged to one challenge, and for the instruction you can do the part 3 first.

Basic command for U-Boot `printenv` like this


[Image extracted text: Request
Response
Pretty
Raw
Hex
5
Pretty
Raw
Hex
Render
GET
pr intenv
HTTP/ 1.1
HTTP / 1.0
200
OF
Host
35.225
17
48:1337
Server
Simpl-HTTP
0.6
Python/ 3
9 . 2
User-Agent
Hozilla/ 5
(Vindous
IT
10.0;
Din64;
x64;
Date
Sun ,
14
Jan
2024
13 : 41:53
GIT
rv:109
Gecko/ -0100101
Firefox/115
Content-type
application/ octet-stream
Accept
Content-Length:
537
cexc
hcml
application  xheml+xml
application xml
4-0.9,im
Last-Hodified:
Thu,
11
Jan
2024 20:36:18
GHT
avif_
image
vebp, * /
9-0.8
Accept-Language
en-US
en;
9-0.5
addmisc-setenv bootargs
Accept-Encodinc:
gzip ,
dleflate
{bootarcs} consolesttySo,
(baudrate} panic=[
Connection:
lose
baudrat--57600
Upgrade-Insecure-Requests:
10
bootaddr- (OxBCOOOOOO
Oxleooo0)
11
bootargs-console-ttysi
57600 rootz/ dev/mtdblock8
10
rts
hconf
hconf
mtd
id-0
mtdparts-m2 5p80:256k (boot )
128k (pib)
1024k
userdata)
128
k(db)
128k ( log)
128k
dbbackup)
128k
logbackup)
3072k(ker
nell
11264k-(rootfs)
12
bootcmd-bootm
Oxbcledou0
13
bootfiles/vlinux
imc
14
ethact-r8168#0
15
ethaddr-00:00
00
00
00:00
16
load-tftp
80500000
u-boot}
loadaddr-0*82000000
13
stderr-serial
19
stdin-serial
20
stdout-serial
21
22
Environment
3i2-:
533
131068
byt-3
23
age/]


And for the part 4, for conclusion we just need trying to init a shell from the part 3 output


[Image extracted text: Baby's First loT
4
476
See introduction for complete context
Part 3 - Submit the command used in U-Boot to look
at the system variables to port 1337asa GET
request ex http.//35.225.17.48.1337 /{command}
This output is needed for another challenge. There is
NO
for this part.
Part 4 - Submit the full command you would use in U-
Boot to set the proper environment variable to a
/bin/sh process upon boot to get the flag on the
webserver at port 7777.Do not include the
'bootcmd' command: It-
be in the format of
'something something-S{something}
something-something'
Submit the answer on port
9123.
Flag
flag-
will]


## How to Solve

We read the description and we are prohibited to use `bootcmd` command, so the alternative is using `bootargs`, because we given some format hint is following like this

`something something=${something} something=something`

To set the environment we can use `setenv` at the start, if you read again the output of part 3 there are already a variable that load some environment


[Image extracted text: bootargs-consolezttysi_
57600
root-/ dev/ mtcblock-8
rts
hconf
hconf
mtd
idx-0
mtdparts-m2 5p80:256k (boot)
128k (pib)
1024}
userdata)
128
cb )
128k(log)
128k
cbbackup)
128k(logbackup)
3072k
ker
nel
1264k(rootfs)]


Then we can make this `bootargs=$bootargs`, for init a shell we use `init=/bin/sh` so we merged up like this

`setenv bootargs=${bootargs} init=/bin/sh`

Submit the answer


[Image extracted text: sinon@LAPTOP- 2VOH1439:
mnt/d/a/bountylctfs
printf
setenv bootargs-f{bootargs}
init-/bingshlnl0'
nc
35
225.17.48
9123
nter
the
command
you
would
use
to
set
the
environment
variables
in
U-Boot
to
boot
the system and
you
shell using
Ibingsh:
Access granted!
The Flag is {Uboot_Hacking} !sinon@LAPTOP-2VOH1439:
mnt/d/a/bountylctfs
give]


```
{Uboot_Hacking}
```