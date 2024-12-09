# New Website
> I made a new site at https://bxmgen2.jonathanw.dev, but my browser gave me this cryptic error code: `DNS_PROBE_FINISHED_NXDOMAIN`

## About the Challenge
As the description said, it looks like the website is broken but we need to find more information by check the website records

## How to Solve?
Check the records of the website using `dig` and the flag was located in the TXT records

```shell
dig bxmgen2.jonathanw.dev TXT
```


[Image extracted text: <<>>
DiG 9.18.1-lubuntul.2-Ubuntu
<<>>
bxmgen2. jonathanw. dev
TXT
global options
+cmd
Got
answer
~>>HEADER<<- opcode:
QUERY
status
NOERROR,
id
17378
flags:
qr
rd
ad
QUERY :
1,
ANSWER :
1,
AUTHORITY:
ADDITIONAL:
WARNING
recursion requested
but
not
available
QUESTION SECTION:
bxmgen2. jonathanw
dev .
IN
TXT
ANSWER  SECTION:
bxmgen2. jonathanw. dev
IN
TXT
"ctf{wlt_whuts_4_txt_r3cOrd}
Query
time
190
msec
SERVER
172.22.176.1#53(172.22.176.1)
(UDP)
WHEN
Sat Jun 03
19:32:50 WIB 2023
MSG SIZE
rcvd
101]


```
ctf{w41t_wh4ts_4_txt_r3c0rd}
```