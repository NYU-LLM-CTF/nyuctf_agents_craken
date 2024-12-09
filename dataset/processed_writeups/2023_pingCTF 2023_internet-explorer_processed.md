# internet-explorer
> Can you run Internet Explorer on Linux?

## About the Challenge
We were given a website without the source code, and this is what the website looks like


[Image extracted text: Can you run Internet Explorer on Linux?]


## How to Solve?
At first I tried to change the `User-Agent` header from `Windows` to `Linux` and I got another response:


[Image extracted text: Request
Response
Pretty
Raw
Hex
3)
In
=
Pretty
Raw
Hex
Render
GET
HTTP/2
HTTP/2
200
OK
2
Host:
internet-explorer
knping. pl
2
Date:
Sun,
10
Dec
2023
13:48:38
GMT
3
Sec-Ch-Ua:
"Chromium"
V="119
"Not?A_Brand" ;V="24"
3 Content-Type:
text/html;
charset-utf-8
User-Agent
Mozilla/5.0
Linuxi
X-Powered-By
Express
5
5
Cf-Cache-Status
DYNAMIC
6
6 Report-To:
{"endpoints"
[{"url":"https: |/|/a.nel.clo
s=WZogwHSfPds
inVTbRYgahGQgYDgtFLS2FWQHNZO
PKBKveHwwwelUSZFdLdIzRvg8VsNbGYas2BqBpqb
kTEZ1S DUWPSes2BcO2QGJcOpfAoES3D"}] ,
groum
4800}
Nel:
{"success_
fraction" :0,"report_to":"c
Server:
cloudflare
Cf-Ray:
8335f24e2edf1069-HKG
10
Alt-Svc:
h3-"
443" ;
ma=86400
11
12
see
Linux
but
no
IE.]


So I googled and found a correct header for Internet Explorer in Linux


[Image extracted text: Request
Response
Pretty
Raw
Hex
3)
In
Pretty
Raw
Hex
Render
GET
HTTP/2
HTTP/2
200
OK
2
Host:
internet-explorer
knping. pl
2
Date:
Sun,
10
Dec
2023
13:50:50
GMT
3
Sec-Ch-Ua:
"Chromium"
V="119
"Not?A_Brand" ;v="24"
3 Content-Type:
text/html;
charset-utf-8
User-Agent
Mozilla/5.0
(Linuxi NT
10.0;
Trident/7.0;
rv: 11.0)
X-Powered-By=
Express
like
Gecko
5
Cf-Cache-Status
DYNAMIC
6 Report-To:
6
{"endpoints"
[{"url":"https: |/|/a.nel.cloudflare.
s=ujCoQoJuJdCyJroskg8BWye8%2BRw%ZBEhFAQ8eQh4aElmQj
2cZaCwmbLZNRlrsZFesYCvDBEFnImJHoN3nssv7qi37zDQpLte
II BcG%2BybqAgMRMSQw%2FYDKmJc%3D"}] ,
group"
:"cf-ne
4800}
Nel:
{"success_
fraction" :0 ,
report_to":"cf-nel" ,
Server:
cloudflare
Cf-Ray:
8335658d4aca1234-HKG
10
Alt-Svc:
h3-"
443"
ma=86400
11
12
<b>
ping {ping{the_best_browser_ever_madel1z}}
b>
Flag]


```
ping{ping{the_best_browser_ever_made111}}
```