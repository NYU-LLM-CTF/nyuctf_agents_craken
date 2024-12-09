# Blue's Clues 5/8: Initial Access
> The web server?? How did the threat actor get access to the web server? Surely we have logs for that... It hosts a simple PHP website, nothing complex.

> Find the malicious file.

> Flag format: <filename>.<fileextension>

> Example: mywebshell.aspx

## About the Challenge
We need to find the name of the webshell

## How to Solve?
Im using this KQL syntax because I want to find the URL that using `PHP` extension and the HTTP response code returned `200 OK`

```
url.extension : php and http.response.status_code : 200
```

And then I searched the log one by one until I found this weird PHP file


[Image extracted text: Discover
New
Open
Share
Alerts
Inspect
logs--
url extension
php and http response.status_code
200
Expanded document
View:
Single document
Surrounding documents
K
204 of 246
hostn
246 hits
Available fields
250
200
source.ip
158. 69.62. 65
150
hosthostname
100
source
port
53, 178
observerhostname
May
June
July
August
2022
status
OK
Apr 15,202:
Empty fields
type
http
No fields match the selected filters_
Documents
Field statistics
url.domain
52.229.123.208
Try:
field sorted
Using different field filters
url
extension
php
@timestamp
Document
url.full
http://52.229.123.208
index. php
command-ls=&p
Meta fields
ZaObf05g-f1c9-4a33-980:
agezuploads"2Fce52790629679d930ca16039a4f619c
t.ip
158 . 69. 62. 65
clie
cloud
machine
type
Apr
12 , 2023
07:37:33 .000
url.extension
php
@tin
url.path
(index.php
ZaObf05g-f1c9-4a33-980
resses
158. 69.62.65
url.query
command-ls-&pagezuploads"2Fce52790629679d930c
a16c39a4f619c3
Standard_B2s
cloud
Apr
12 ,
2023
07:37:26 . 845
url.extension
php
@tin
url.scheme
http
ZaObf05g-f1c9-4a33
980-
t.ip 158.69.62.65
clie
user_agent.original
Mozilla/5.0
(X11;
Linux
x86_
64 ;
rv:109.0)
Gec
cloud.machine
type
ko/20100101
Firefox/111.0
Apr
12,
2023
07:37:26.000
url.extension
php
@tin
Rows per page: 100
<1
2
Rows per page: 500]


```
ce52790629679d930ca16c39a4f619c3.php
```