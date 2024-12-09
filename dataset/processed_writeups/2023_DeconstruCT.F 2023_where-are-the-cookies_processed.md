# where-are-the-cookies
> Tom is feeling especially snacky during the CTF, can you find where the cookies are?

> Note: This challenge works best on Chrome

## About the Challenge
We got a very simple website and we need to find the flag in the website


[Image extracted text: 6 
C
ch29524130545.chengrun
Welcome to the kitchen! Where are the cookies?]


## How to Solve?
First, we need to find some common files such as `robots.txt` / `sitemap.xml`. And in this case, this website have a `robots.txt` file


[Image extracted text: < 
C
ch29524130545.cheng run/robots.txt
User-
Disallow:
[cookiesaretotallynothere
agent:]


We discovered another endpoint called `/cookiesaretotallynothere`. When we hit the endpoint, there is a cookie called `caniseethecookie`


[Image extracted text: 6 >
C
ch29524130545.ch eng-run/cookiesaretotallynothere
No cookies for you todayl
Cookie Editor
Show Advanced
Search
caniseethecookie
Name
caniseethecookie
Value
bm8==
ShoW Advanced]


Decode the value of the cookie using `base64`


[Image extracted text: Decoue Trom Dase0y Tonat
Simply enter your data then push the decode button.
bm8-=
For encoded binaries (like images
documents
UTF-8
source character set 
Decode each Iine separately (useful for when you
Live mode ON
Decodes in real-lime as VOE
DECODE
Decodes your data into the]


Change from `no` into `yes` and then encode the message again using `base64` encoding


[Image extracted text: ch29524130545.
run/cookiesaretotallynothere
You found the cookiel
Oh; Ialso found this unrelated string; might be useful to you: dsc{c0Okl35_4r3_th3_cOoL3St}
Cookie Editor
Show Advanced
Search
caniseethecookie
Name
caniseethecookie
Value
eWVz
Show Advanced
cheng:]


```
dsc{c0Ok135_4r3_th3_c0oL35t}
```