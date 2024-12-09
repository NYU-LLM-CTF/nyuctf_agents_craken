# A Network Problem - Part 1
> There are some interesting ports open on betta.utctf.live, particularly port 8080.

## About the Challenge
We were given a server to connect `betta.utctf.live:8080`

## How to Solve?
To get the flag you need to connect to the server using `nc`


[Image extracted text: daffainfo@LAPTOP-F9LBRGSH:~$
nc
betta.utctf.live 8080
Hi Wade!
am
using socat
to broadcat this message. Pretty nifty right?
jwalker utflag{meh-netcats-cooler}]


```
utflag{meh-netcats-cooler}
```