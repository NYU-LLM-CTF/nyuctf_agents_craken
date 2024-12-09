# Just Explore!
> Just explore and find a vulnerability innit :)

> http://0x7e7ctf.zerobyte.me:49723/

## About the Challenge
Given a website without the source code and on the main page, there's an endpoint named `/explore` which contains a somewhat random file.


[Image extracted text: 6 >
C
Not secure
OxTe/ctfzerobyte me.49723/explore/
Index of /explorel
@byteCIE2023-Banner_ jpg
17-Aug-2023
20:45
31972
Bocchi_jpg
2023 20:45
103784
Sakura-Miko_jpg
17-Aug-2023 20:45
123323
Yoimiya_jpg
17-Aug-2023 20:45
58140
favicon.ico
17-Aug-2023 20:45
4286
inti
bumi
txt
17-Aug-2023
20:45
17-Aug-]


## How to Solve?
If you observe the HTTP response header and see that the site is using NGINX as the web server, there's a possibility that the site might be vulnerable to path traversal if there's a misconfiguration in NGINX. An example of this can be seen on a site like this: https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/. To perform path traversal, you'd need to add `../` to the URL after `explore`.


[Image extracted text: Not secure
OxTeTctfzerobyte me 49723/explore 
Index of /explore_/
hin
16-Aug-2023
09:50
hootz
14-Jul-2023 16:00
datal
17-Aug-2023 29:48
devL
19-Aug-2023
b:
docker-
entcypoint_dL
16-Aug_
etcL
19-Aug
3
ocmel
14-Jul
16:=
libz
16-Aug-2023
1ib324
14-Aug
80;08
libeal
14-Aug
00;o8
libx3L
14-Aug;
03:06
medial
14-Aug
9
mntL
14-Aug;
39.96
PPEL
14-Aug_
83:08
FLOSL
19-Aug-2023
Cc oi/
14-Aug-2023 83:08
Cudz
19-Aug-2023
sbinz
16-Aug
2023
sVL
14-Aug-2023 88:00
SysL
19-Aug:
2023
44.31
ImpL
16-Aug-2023
09:56
WScL
14-Aug-2023 83:00
Tari
2023 28:48
docker-entrypoint_sh
16-Aug-2023 09:50
1620
-Aug-]


And my suspicion is correct; the site is vulnerable to path traversal. The next step is to find the `flag.txt` file on the server, and after searching for a while, the flag is located in the directory `/usr/share/flag.txt`.


[Image extracted text: OxTe7ctfzerobyte me:49723/explor X
Secure Login
OxTe7ctfzerobyte me 49723/explore-/usr /share/flag txt
ObyteCTF{Path_TrAv3rSAL_ThRu_NglnX_MlsCOnflg_4114s}]


```
0byteCTF{P4th_Tr4v3rS4L_ThRu_Ng1nX_M1sC0nf1g_4l14s}
```